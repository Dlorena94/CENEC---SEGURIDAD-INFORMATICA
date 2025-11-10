param(
  [int]$WebPort = 80,      # Puerto web externo -> interno 80
  [int]$SrvPort = 10051      # Puerto Zabbix server
)

$ErrorActionPreference = "Stop"

Write-Host "==> Comprobando Docker Desktop..."
try { docker version | Out-Null } catch {
  Write-Error "Docker Desktop no está instalado o no está corriendo. Ábrelo e inténtalo de nuevo."
  exit 1
}

if ($WebPort -lt 1 -or $WebPort -gt 65535) { throw "WebPort inválido." }
if ($SrvPort -lt 1 -or $SrvPort -gt 65535) { throw "SrvPort inválido." }

$Project     = "zabbix"
$BaseDir     = Join-Path $env:USERPROFILE "zabbix"
$ComposePath = Join-Path $BaseDir "docker-compose.yml"

Write-Host "==> Creando carpeta de stack: $BaseDir"
New-Item -ItemType Directory -Force -Path $BaseDir | Out-Null

# docker-compose.yml mínimo (MySQL 8 + Zabbix Server + Web)
$compose = @"
services:
  db:
    image: mysql:8
    environment:
      MYSQL_DATABASE: zabbix
      MYSQL_USER: zabbix
      MYSQL_PASSWORD: zabbix
      MYSQL_ROOT_PASSWORD: rootpass
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_bin
    volumes:
      - dbdata:/var/lib/mysql

  zabbix-server:
    image: zabbix/zabbix-server-mysql:alpine-latest
    environment:
      DB_SERVER_HOST: db
      MYSQL_DATABASE: zabbix
      MYSQL_USER: zabbix
      MYSQL_PASSWORD: zabbix
    depends_on: [db]
    ports:
      - "${SrvPort}:10051"

  zabbix-web:
    image: zabbix/zabbix-web-nginx-mysql:alpine-latest
    environment:
      DB_SERVER_HOST: db
      MYSQL_DATABASE: zabbix
      MYSQL_USER: zabbix
      MYSQL_PASSWORD: zabbix
      ZBX_SERVER_HOST: zabbix-server
      PHP_TZ: Europe/Madrid
    depends_on: [zabbix-server]
    ports:
      - "${WebPort}:8080"

volumes:
  dbdata:
"@
$compose | Out-File -FilePath $ComposePath -Encoding UTF8 -Force

Write-Host "==> Levantando Zabbix en puertos Web=$WebPort, Server=$SrvPort..."
docker compose -p $Project -f $ComposePath up -d

Start-Sleep -Seconds 4
Write-Host "==> Listo."
Write-Host "   - Web:  http://localhost:$WebPort"
Write-Host "   - Puesto del servidor (para agentes): $SrvPort"
Write-Host "   - Usuario inicial: Admin   Contraseña: zabbix"
Write-Host ""
Write-Host "Siguientes pasos:"
Write-Host "  1) Abre la web y completa el asistente si te lo pide."
Write-Host "  2) Entra con Admin/zabbix y cambia la contraseña."
Write-Host "  3) Crea tu primer host y aplica un template."
try { Start-Process "http://localhost:$WebPort" } catch {}
