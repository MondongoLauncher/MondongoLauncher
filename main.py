import os
import json
import time
import subprocess
import asyncio
import minecraft_launcher_lib


VERSION = ('1.0.0')
user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.minecraft"
ruta_json = f"{minecraft_directory}//configuration.json"

async def check():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists(minecraft_directory):
        os.makedirs(minecraft_directory)

    if not os.path.exists(ruta_json):
        # Si el archivo JSON no existe, crea uno vacío
        with open(ruta_json, 'w') as f:
            print("Archivo config.json no encontrado.")
            time.sleep(1)
            print("Se ha creado el archivo config.json.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Introduce un nombre de usuario:')
            nombre = input('» ')
            if nombre == "":
                print('Nombre no válido')
                time.sleep(2)
                await check()
            else:
                print('Introduce cuánta RAM se utilizará (4GB recomendado):')
                ram = input('» ')
                if ram == "":
                    print('RAM no válida')
                    time.sleep(2)
                    await check()
                else:
                    data = {
                        "Nombre": nombre,
                        "RAM": ram,
                    }
                    with open(ruta_json, 'w') as file:
                        json.dump(data, file)
                    print("◈ Guardando... ◈")
                    time.sleep(2)
                    await menu_I()
    else:
        # Si el archivo JSON existe, pero está vacío, accede a él
        if os.stat(ruta_json).st_size == 0:
            print("El archivo config.json está vacío.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Introduce un nombre de usuario:')
            nombre = input('» ')
            if nombre == "":
                print('Nombre no válido')
                time.sleep(2)
                await check()
            else:
                print('Introduce cuánta RAM se utilizará (4GB recomendado):')
                ram = input('» ')
                if ram == "":
                    print('RAM no válida')
                    time.sleep(2)
                    await check()
                else:
                    data = {
                        "Nombre": nombre,
                        "RAM": ram,
                    }
                    with open(ruta_json, 'w') as file:
                        json.dump(data, file)
                    print("◈ Guardando... ◈")
                    time.sleep(2)
                    await menu_I()
        else:
            await menu_I()

async def menu_I():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(ruta_json, 'r') as file:
        data = json.load(file)
    nombre = data.get('Nombre')

    print(
        f'''               
                    ███╗   ███╗ ██████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ██╗ ██████╗  ██████╗ 
                    ████╗ ████║██╔═══██╗████╗  ██║██╔══██╗██╔═══██╗████╗  ██║██╔════╝ ██╔═══██╗
                    ██╔████╔██║██║   ██║██╔██╗ ██║██║  ██║██║   ██║██╔██╗ ██║██║  ███╗██║   ██║
                    ██║╚██╔╝██║██║   ██║██║╚██╗██║██║  ██║██║   ██║██║╚██╗██║██║   ██║██║   ██║
                    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝
                    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
                                                                                            
                    ██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗         
                    ██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗        
                    ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝        
                    ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗        
                    ███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║        
                    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ versión {VERSION}

                    
Bienvenido a MondongoLauncher, {nombre}\n

▐Jugar Minecraft (1)
▐Instalar una versión Vanilla (2)
▐Instalar una versión Forge (3)
▐Instalar una versión Fabric (4)
▐Instalar un modpack (5)
▐Editar config.json (6)
▐Info (7)
▐----------------------
▐Salir (0)
''')

    select = input('Selecciona un opción: ')
    if select == "1":
        await play_mine()
    elif select == "2":
        await install_minecraft()
    elif select == "3":
        await install_forge()
    elif select == "4":
        await install_fabric()
    elif select == "5":
        await install_modpack()
    elif select == '6':
        await cambiar_config()
    elif select == '7':
        await info_app()
    elif select == "0":
        exit()
    elif select == "":
        await menu_I()
    else:
        print("\n>>Selecciona un número del 0 al 7<<")
        time.sleep(2)
        await menu_I()



# Indicador de por donde va la instalación
current_max = 0

def set_status(status: str):
    print(status)


def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")


def set_max(new_max: int):
    global current_max
    current_max = new_max

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}



async def cambiar_config():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(ruta_json, 'r') as file:
        data = json.load(file)

    print("▨ Valores actuales ▨")
    for key, value in data.items():
        print(f"▸ {key}: {value}")
    print('\n¿Qué dato deseas cambiar? (Nombre/RAM) (o pulsa Enter para volver)')
    option = input('» ')
    if option == "":
       await menu_I()
    else:
        print('Opción no válida')
        time.sleep(1)
        await info_app()
        if option in data:
            print(f'Ingresa el nuevo valor para {option}')
            nuevo_valor = input('» ')
            data[option] = nuevo_valor

            with open(ruta_json, 'w') as file:
                json.dump(data, file)

            print(f"◈ Actualizando... ◈")
            time.sleep(2)
            await menu_I()
        else:
            print("Opción no válida. Por favor, elije entre Nombre o RAM")
            await cambiar_config()



async def info_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(ruta_json, 'r') as file:
        data = json.load(file)

    print("\n▨ Info de Usuario ▨")
    for key, value in data.items():
        print(f"    ▸ {key}: {value}")

    print("\n▨ Info del launcher ▨")
    print(
        f'''
    »Launcher simple para jugar Minecraft de manera no premium, con opciones apra descargar Forge, Fabric y modpacks.

    »Versión: {VERSION}\n
''')
    print('Pulsa Enter para volver')
    sel = input('» ')
    if sel == "":
       await menu_I()
    else:
        print('Opción no válida')
        time.sleep(1)
        await info_app()


#------------------------------------------------------


# Instalar Minecraft
async def install_minecraft():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecciona la versión que quieras instalar (o pulsa enter para volver):")
    minecraft_version = input('» ')
    if minecraft_version == "":
       await menu_I()
    else:
        valid = minecraft_launcher_lib.utils.is_version_valid(minecraft_version, minecraft_directory)
        if valid == True:
            minecraft_launcher_lib.install.install_minecraft_version(minecraft_version, minecraft_directory, callback=callback) # type: ignore
            print(f'» Instalada la version {minecraft_version}')
            await menu_I()
        else:
            print(f'{minecraft_version} no es una versión de Minecraft :(')
            time.sleep(2)
            await install_minecraft()


# Instalar Forge
async def install_forge():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Introduce la versión de Minecaft con Forge a instalar (o pulsa Enter para volver):')
        forge_ver = input('» ')
        if forge_ver == "":
            await menu_I()
        else:
            forge = minecraft_launcher_lib.forge.find_forge_version(forge_ver)
            print(forge)
            minecraft_launcher_lib.forge.install_forge_version(forge, minecraft_directory, callback=callback) # type: ignore
            print("◈ Forge Instalado... ◈")
            time.sleep(2)
            await menu_I()
        

#Instalar Fabric
async def install_fabric():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Introduce la versión de Minecraft con Fabric a instalar (o pulsa Enter para volver):')
    fabric_ver = input('» ')
    if fabric_ver == "":
       await menu_I()
    else:
        fabric_suport_ver = minecraft_launcher_lib.fabric.is_minecraft_version_supported(fabric_ver)
        if fabric_suport_ver == False:
            print('Fabric no es compatible con esta versión')
            time.sleep(2)
            await install_fabric()
        else:
            fabric = minecraft_launcher_lib.fabric.install_fabric(fabric_ver, minecraft_directory, callback=callback) # type: ignore
            print("◈ Fabric Instalado... ◈")
            time.sleep(2)
            await menu_I()


#Jugar Minecraft
async def play_mine():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(ruta_json, 'r') as file:
        data = json.load(file)

    if 'Nombre' in data and 'RAM' in data:
        mine_user = data['Nombre']
        ram = data['RAM']

    options = {
        'username': mine_user,
        'uuid': '',
        'token': '',

        "jvmArguments": [f"-Xmx{ram}G",f"-Xms{ram}G"],  # The jvmArguments
        
        "launcherVersion": VERSION,
        "launcherName": "MondongoLauncher"
    }

    forts = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
    print("\n▨ Versiones instaladas ▨")
    for fort in forts:
        print(fort['id'])
    print(
        f'''
Selecciona una versión instalada(o pulsa Enter para volver):''')
    version = input('» ')
    if version == "":
       await menu_I()
    else:

        valid = minecraft_launcher_lib.utils.is_version_valid(version, minecraft_directory)
        if valid == True:
            # Ejecutar Minecraft
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options) # type: ignore
            subprocess.run(minecraft_command)
        else:
            print(f'{version} no es una versión de Minecraft :(')
            time.sleep(2)
            await play_mine()



async def install_modpack():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Introduce la ruta del archivo .mrpack (o pulsa Enter para volver):")
    mrpack_path = input('» ')
    if mrpack_path == "":
       await menu_I()
    else:

        if not os.path.isfile(mrpack_path):
            print(f"{mrpack_path} no fue encontrado")
            await install_modpack()

        try:
            mrpack_information = minecraft_launcher_lib.mrpack.get_mrpack_information(mrpack_path)
        except Exception:
            print(f"{mrpack_path} no es un archivo .mrpack válido")
            await install_modpack()

        # Print some Information
        print("Has seleccionado el siguiente modpack:")
        print("Nombre: " + mrpack_information["name"])
        print("Descripción: " + mrpack_information["summary"])
        print("Versión de Minecraft: " + mrpack_information["minecraftVersion"])


        print("¿Quieres instalar este modpack? [Y/N]")
        answer = input('» ').strip().upper()
        if answer == "Y":
            # Ask the User for the Directories
            print("Introduce la ruta a la carpeta de Minecraft (dejar vacío para seleccionar la carpeta por defecto):")
            minecraft_directory = input('» ')

            if minecraft_directory == "":
                minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

            print("Introduce la ruta en la que quieras instalar este modpack (dejar vacío para seleccionar la carpeta de Minecraft):")
            modpack_directory = input('» ')

            if modpack_directory == "":
                modpack_directory = minecraft_directory

            # Adds the Optional Files
            mrpack_install_options: minecraft_launcher_lib.types.MrpackInstallOptions = {"optionalFiles": []}
            for i in mrpack_information["optionalFiles"]:
                print(f"El mopack contiene el archivo opcional {i}. ¿Quieres instalarlo?")
                answer = input('» ').strip().upper()
                if answer == "Y":
                    mrpack_install_options["optionalFiles"].append(i)

            # Install
            print("Instalando...")
            minecraft_launcher_lib.mrpack.install_mrpack(mrpack_path, minecraft_directory, modpack_directory=modpack_directory, mrpack_install_options=mrpack_install_options, callback={"setStatus": print})
            print("Terminado")
            time.sleep(2)
            await menu_I()

        elif answer == "N":
            print('Volviendo al menú')
            time.sleep(2)
            await menu_I()
        else:
            print("Respuesta no válida. Utiliza Y o N")


async def inicio():
    await check()

if __name__ == '__main__':
    asyncio.run(inicio())
