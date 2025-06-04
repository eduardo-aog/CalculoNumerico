import os

class ArchiveUtil():
    __router = ""

    def __init__(self, router = os.getcwd()):#constructor polimorfico
        if (not router or len(router) == 0):
            raise Exception("Manage-Error: La ruta es vacia.")
        self.utilDirectory(router)

    #getters    
    def getRouter(self):
        return str(self.__router)
    
    def getArchive(self, nameArchive):

        if (not nameArchive or len(nameArchive) == 0):
            raise Exception("Manage-Error: El nombre esta Vacio.")
        
        try: #usamos try en este constexto ya que OPEN es un objeto externo a nuestra clase
            archive = open(self.__router+"\\"+nameArchive)#requiere que el nombre venga con su extencion. 
            return archive
        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)
            return None

    def getDirectoriesList(self):

        try:#usamos try en este constexto ya que OPEN es un objeto externo a nuestra clase
            directories = os.listdir(self.__router)  # Obtiene la lista de archivos y directorios

            if (len(directories) > 0):
                return directories
            else:
                raise FileNotFoundError("No se encontraron archivos.")

        except FileNotFoundError as e:
            print("Manage-Error: Directorio no existe: ", e)
            return None

        except NotADirectoryError as e:
            print("Manage-Error: Ocurrió un error inesperado:", e)
            return None
        
    #setters
    """
    *Cambio de ruta existente
    *@param: string router = C:\\folder1\\folder2\\folder or r"C:\folder\folder\folder" or C:/folder/folder/folder
    *@return: 
    """
    def setRouter(self, router):
        if (not router or len(router) == 0):
            raise Exception("Manage-Error: La ruta es vacia.")
        self.utilDirectory(router)

    def setOrCreateFiles(self, nameArchive, content = "", bool = False):#metodo polimorfico

        if (not nameArchive or len(nameArchive) == 0):
            raise Exception("Manage-Error: El nombre esta Vacio.")
        
        
        try: #usamos try en este constexto ya que OPEN es un objeto externo a nuestra clase
            if (not content or len(content) == 0):
                archive = open(self.__router+"\\"+nameArchive+".txt", "x")
                return
            
            archive = open(self.__router+"\\"+nameArchive, "a")#requiere que el nombre venga con su extencion. 
            
            if (bool == True):
                archive.write(content+"\n")
            else:
                archive.write(content)

        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)

    #utilitarias
    def utilDirectory(self, router):
        
        if (os.path.exists(router) and not os.path.isdir(router)):
            raise NotADirectoryError(f"Manage-Error: La ruta '{router}' no es un directorio.")
        elif (not os.path.exists(router)):
            raise FileNotFoundError(f"Manage-Error: El directorio '{router}' no existe.")
        
        self.__router = router