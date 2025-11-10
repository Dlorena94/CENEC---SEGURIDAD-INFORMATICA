param(
  [int]$PrometheusPort = 9090,
  [string[]]$ExtraTargets = @("linuxvm:9100","winhost:9182")
)

$ErrorActionPreference = "Stop"

# 1) Comprobar Docker
Write-Host "==> Comprobando Docker Desktop..."
try { docker version | Out-Null } catch {
  Write-Error "Docker Desktop no está instalado o no está corriendo. Ábrelo e inténtalo de nuevo."
  exit 1
}

# 2) Validar puerto
if (-not $PrometheusPort -or $PrometheusPort -lt 1 -or $PrometheusPort -gt 65535) {
  Write-Error "Puerto inválido ($PrometheusPort). Usa un valor entre 1 y 65535."
  exit 1
}
$PortMap = "{0}:9090" -f $PrometheusPort

# 3) Rutas
$ProjectName = "prometheus"
$BaseDir     = Join-Path $env:USERPROFILE "prometheus"
$ConfDir     = Join-Path $BaseDir "config"
$ComposePath = Join-Path $BaseDir "docker-compose.yml"
$PromCfgPath = Join-Path $ConfDir "prometheus.yml"

# 4) Crear carpetas
Write-Host "==> Creando carpetas en $BaseDir"
New-Item -ItemType Directory -Force -Path $ConfDir | Out-Null

# 5) Generar prometheus.yml
$targetsYaml = @('"prometheus:9090"')
foreach ($t in $ExtraTargets) { if ($t.Trim()) { $targetsYaml += ('"'+$t.Trim()+'"') } }
$targetsLine = "[{0}]" -f ($targetsYaml -join ", ")

$promCfg = @"
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["prometheus:9090"]

  - job_name: "infra"
    static_configs:
      - targets: $targetsLine
"@
$promCfg | Out-File -FilePath $PromCfgPath -Encoding UTF8 -Force

# 6) docker-compose.yml (siempre con puerto definido)
$compose = @"
services:
  prometheus:
    image: prom/prometheus:latest
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.retention.time=15d"
    volumes:
      - ./config/prometheus.yml:/etc/prometheus/prometheus.yml:ro
    ports:
      - "$PortMap"
    container_name: prometheus
"@
$compose | Out-File -FilePath $ComposePath -Encoding UTF8 -Force

# 7) Levantar stack
Write-Host "==> Levantando Prometheus (puerto $PrometheusPort)..."
docker compose -p $ProjectName -f $ComposePath up -d --force-recreate

Start-Sleep -Seconds 2
Write-Host "==> Listo. Abre: http://localhost:$PrometheusPort"
Write-Host "   - En Grafana, añade Prometheus como Data source: http://prometheus:9090 (si están en el mismo docker network)."

