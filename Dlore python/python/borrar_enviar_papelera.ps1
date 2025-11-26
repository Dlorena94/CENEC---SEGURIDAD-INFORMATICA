$trash = "$env:USERPROFILE\Trash"
New-Item -ItemType Directory -Force -Path $trash | Out-Null
Move-Item -LiteralPath "RUTA\al\archivo.ext" -Destination $trash