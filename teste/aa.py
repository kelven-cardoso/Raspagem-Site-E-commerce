from selenium import webdriver

class web():
    def __init__(self):
        
        self.abrir_navegador()
        self.ver_preco()


    def abrir_navegador(self):
        self.navegador = webdriver.Chrome()
        self.navegador.set_window_size(800,700)
        self.navegador.get('https://telefonesimportados.netlify.app/')
        print('voce esta no site: ', self.navegador.title) 
        self.lista_nome_celulares = []
        self.lista_preco_celulares = []
        
    def ver_preco(self):
        for p in range(5):
            lista_nome = self.navegador




def main():
    start = web()
    
    
    



if __name__ == "__main__":
    main()