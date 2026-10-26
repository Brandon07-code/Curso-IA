$ErrorActionPreference = "Stop"

$ffmpeg = "C:\Users\Brandon\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
$baseDir = "C:\Users\Brandon\Desktop\CursoIA\material_video"
$audioDir = "$baseDir\audios"
$slideDir = "$baseDir\slides"
$tempDir = "$baseDir\temp_segments"

if (!(Test-Path $tempDir)) {
    New-Item -ItemType Directory -Path $tempDir | Out-Null
}

Write-Host "=== ENSAMBLANDO VIDEO DE SUSTENTACIÓN PAVIA ===" -ForegroundColor Cyan

# Función para generar segmento de imagen estática + audio
function Build-ImageSegment {
    param(
        [string]$ImgPath,
        [string]$AudioPath,
        [string]$OutPath
    )
    Write-Host "Generando segmento: $(Split-Path $OutPath -Leaf)..." -ForegroundColor Yellow
    & $ffmpeg -y -loop 1 -framerate 30 -i $ImgPath -i $AudioPath `
        -c:v libx264 -preset veryfast -crf 20 -tune stillimage -pix_fmt yuv420p `
        -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30" `
        -c:a aac -b:a 192k -ar 48000 -ac 2 `
        -shortest $OutPath
}

# Segmento 1
Build-ImageSegment -ImgPath "$slideDir\slide_01_portada.png" `
                   -AudioPath "$audioDir\01_brandon_intro_problematica.ogg" `
                   -OutPath "$tempDir\seg_01.mp4"

# Segmento 2
Build-ImageSegment -ImgPath "$slideDir\slide_02_objetivos.png" `
                   -AudioPath "$audioDir\02_johan_objetivos_ml.ogg" `
                   -OutPath "$tempDir\seg_02.mp4"

# Segmento 3
Build-ImageSegment -ImgPath "$slideDir\slide_03_datos_limpieza.png" `
                   -AudioPath "$audioDir\03_johan_datos_limpieza.ogg" `
                   -OutPath "$tempDir\seg_03.mp4"

# Segmento 4
Build-ImageSegment -ImgPath "$slideDir\slide_04_seaborn.png" `
                   -AudioPath "$audioDir\04_brandon_seaborn.ogg" `
                   -OutPath "$tempDir\seg_04.mp4"

# Segmento 5: Clip de Terminal Docker (42.2s) + Slide Perceptrón (26.55s) + Audio Brandon (68.75s)
Write-Host "Generando segmento 5 (Terminal Docker + Slide Perceptrón)..." -ForegroundColor Yellow
$clipPath = "$baseDir\terminal_docker_clip.mp4"
$slide5Path = "$slideDir\slide_05_perceptron_resultados.png"
$audio5Path = "$audioDir\05_brandon_perceptron_docker.ogg"
$out5Path = "$tempDir\seg_05.mp4"

$filterComplex = "[0:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,trim=duration=42.199,setpts=PTS-STARTPTS[v0]; [1:v]fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,trim=duration=26.548,setpts=PTS-STARTPTS[v1]; [v0][v1]concat=n=2:v=1:a=0[v]"

& $ffmpeg -y -i $clipPath -loop 1 -framerate 30 -i $slide5Path -i $audio5Path `
    -filter_complex $filterComplex -map "[v]" -map "2:a" `
    -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p `
    -c:a aac -b:a 192k -ar 48000 -ac 2 `
    -shortest $out5Path

# Segmento 6
Build-ImageSegment -ImgPath "$slideDir\slide_06_proximos_pasos.png" `
                   -AudioPath "$audioDir\06_johan_proximos_pasos.ogg" `
                   -OutPath "$tempDir\seg_06.mp4"

# Archivo de concatenación
$concatListFile = "$tempDir\concat_list.txt"
$concatContent = @"
file 'seg_01.mp4'
file 'seg_02.mp4'
file 'seg_03.mp4'
file 'seg_04.mp4'
file 'seg_05.mp4'
file 'seg_06.mp4'
"@
Set-Content -Path $concatListFile -Value $concatContent -Encoding ASCII

# Concatenar todos los segmentos
$finalVideoCourse = "$baseDir\Avance2_Grupo04_PAVIA.mp4"
$finalVideoDesktop = "C:\Users\Brandon\Desktop\Avance2_Grupo04_PAVIA.mp4"

Write-Host "Concatenando video final completo..." -ForegroundColor Green
& $ffmpeg -y -f concat -safe 0 -i $concatListFile -c copy $finalVideoCourse
Copy-Item -Path $finalVideoCourse -Destination $finalVideoDesktop -Force

Write-Host "=== VIDEO FINAL COMPLETADO CON ÉXITO ===" -ForegroundColor Green
Write-Host "Ubicación 1: $finalVideoCourse"
Write-Host "Ubicación 2: $finalVideoDesktop"
