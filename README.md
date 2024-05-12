# ¡Bienvenid@ a MondongoLauncher! 👋

MondongoLauncher es un launcher personalizado de Minecraft ligero y simple, hecho con Python y la librería [minecraft-launcher-lib](https://github.com/JakobDev/minecraft-launcher-lib), en el que puedes:

  - Instalar cualquier versión de Minecraft
  - Instalar Forge
  - Instalar Fabric
  - Instalar modpacks de [Modrinth](https://modrinth.com/)

    

## Instalación
- Dirígete a [Releases](https://github.com/MondongoLauncher/MondongoLauncher/releases) y descarga la última versión de `MondongoLauncher.zip`
- Una vez descargado, descomprímelo y ejecuta `MondongoLauncher.exe`

## Problemas con Windows Defender
  
> [!CAUTION]  
> **SI DESCONFÍAS DE QUE EL PROGRAMA TENGA VIRUS, PUEDES REVISAR EL CÓDIGO ORGINAL ABRIENDO [main.py](https://github.com/MondongoLauncher/MondongoLauncher/blob/4bd396d2ffe3b9e233ddd9523d1d74e3f47f3e98/main.py)     EN LA PÁGINA DE INICIO**
  
  - Al ejecutar por primera vez el programa, debería aparecer una ventana como esta:

  ![preview](https://github.com/MondongoLauncher/MondongoLauncher/blob/0ff6f5bb72bb64b6b3426acd8be9afba935fef67/assets/Alerta.png)
  - Esto se debe a que el programa no está firmado digitalmente. Explicando esto de una forma resumida, *se trata de firmar digitalmente el ejecutable con un certificado emitido por una autoridad de                  certificación (CA) de confianza, lo cual mejora la legitimidad de la aplicación y reduce la probabilidad de desencadenar detecciones antivirus*
    
  - Todo esto es muy bueno, hasta que descubres que tienes que pagar como 60 pavos al mes para mantener el certificado. Obviamente no lo voy a hacer, por eso aparece la ventana arriba mencionada. Para permitir       que Windows ejecute el programa, haz clic en "Más opciones" y después en "Ejecutar de todas formas"




## Uso del programa
- Ejecuta `MondongoLauncher.exe`
- Si es la primera vez que utilizas este programa, te pedirá que introduzcas un nombre de usuario y cuanta RAM quieres que utilize el juego (recomendado 4 GB)
- Una vez terminado el proceso de configuración, debería aparecer una pantalla como esta:

  ![preview](https://github.com/MondongoLauncher/MondongoLauncher/blob/27abb01e7e8696fcb662e776a87ce66e37abaaf4/assets/Captura%20de%20pantalla.png)

  A partir de aquí, tan solo sigue las instrucciones del programa

## Instalar modpacks
- Ve a [Modrinth](https://modrinth.com/modpacks) y busca cualquier modpack que quieras
- Una vez dentro, baja hasta la parte de descargas
- Selecciona la versión compatible con tu Minecraft y pulsa el botón verde que dice "Download"
- Una vez descargado, ejecuta MondongoLauncher y selecciona la opción 5: Instalar un modpack
- Te pedirá que introduzcas la ruta del modpack a descargar
- Para ello, abre el Explorador de archivos y ve donde se encuentra el archivo
- Seleccionalo, haz clic derecho sobre él y elige "Copiar como ruta de acceso" o Ctrl+Shift+C
- Vuelve a la ventana de MondongoLaucher y pulsa Ctrl+V
- Pegará la ruta del archivo, pero añadiendo unas comillas al principio y al final. Simplemente bórralas.
- Pulsa Enter y lo demás es seguir las instrucciones del programa.

## Desinstalar
- Para desinstalar el programa, simplemente borra la carpeta donde se encuentra el programa
- ¡Tan simple como eso!

  
- Recuerda que esto solo desinstala el launcher, la carpeta .minecraft todavía existe en tu pc.
- Para borrarla, pulsa Win+R y escribe %AppData%
- Aparecerá una pequeña ventana abajo a la izquierda:
  
  ![preview](https://github.com/MondongoLauncher/MondongoLauncher/blob/72cb6e0a75a4df8219d9ed7570bd5bba0f95ebd3/assets/Win%2BR.png)

- Dale al Enter y se abrirá el Explorador de archivos
- Selecciona la carpeta .minecraft y simplemente bórrala

## Créditos

- [KeimaSenpai](https://github.com/KeimaSenpai), por crear [XLauncher](https://github.com/KeimaSenpai/XLauncher-Script), projecto en el que se basa todo esto
