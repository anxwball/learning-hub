param(
  [string]$Dir = 'lenguajes\python\100_ejercicios',
  [int]$Start = 1,
  [int]$End = 100,
  [switch]$Force,
  [switch]$NoReplace
)

$root = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$target = Join-Path $root $Dir
New-Item -ItemType Directory -Path $target -Force | Out-Null

for ($i = $Start; $i -le $End; $i++) {
  $fileName = "Ejercicio_$i.py"
  $path = Join-Path $target $fileName

  $content = @"
"""
Problema  : 
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : $(Get-Date -Format yyyy-MM-dd)
Estado    : por revisar

Enfoque:
    -

Complejidad: Tiempo O() | Espacio O()

Casos límite:
    -

Revisión:
    -
"""

def main():
    """plantilla base"""
    pass

if __name__ == '__main__':
    main()
"@

  if (Test-Path $path) {
    if ($NoReplace) {
      Write-Host "Skipping existing $fileName (NoReplace)"
      continue
    } else {
      Write-Host "Updating $fileName"
    }
  } else {
    Write-Host "Creating $fileName"
  }

  $content | Out-File -FilePath $path -Encoding UTF8 -Force
}