from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import pyautogui

def main ():
    try:
        #abrir o navegador com o site
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://ic360.com.br/")

        # Esperar até que o botão "acessar" seja visível e interagível
        acessar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'acessar')]"))
        )

        # Preencher o campo de usuário após o botão "acessar" ser visível
        login = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "UserName"))
        )
        login.send_keys("07039312964_48884")
        login.send_keys(Keys.TAB)

        # Preencher o campo de senha após o botão "acessar" ser visível
        senha = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "Passwd"))
        )
        senha.send_keys("Lais2023@")

        # Clicar no botão "acessar"
        acessar_button.click()

        elemento_apos_login = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > canal360i-root > canal360i-page-build > div > main > div > div > canal360i-controlador-pagina > div > div > div > canal360i-wrapper-mfe-strategy > canal360i-wrapper-mfe > div.container.ng-star-inserted > mf-corbans-chassi'))
        )

        # Espera explícita para o primeiro Shadow Host
        shadow_host1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > canal360i-root > canal360i-page-build > div > main > div > div > canal360i-controlador-pagina > div > div > div > canal360i-wrapper-mfe-strategy > canal360i-wrapper-mfe > div.container.ng-star-inserted > mf-corbans-chassi'))
        )
        shadow_root1 = driver.execute_script('return arguments[0].shadowRoot', shadow_host1)

        # Espera explícita para o segundo Shadow Host
        shadow_host2 = WebDriverWait(shadow_root1, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#home > div > microfrontend-corbans-chassi-base-pagina-padrao > section > div > microfrontend-corbans-chassi-inss > mf-corban-inss'))
        )
        shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', shadow_host2)

        # Espera explícita para o elemento dentro do segundo Shadow Root
        elemento_cpf = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#voxel-input-0'))
        )
        cpf_original = '77551460225'  # <<<<<<<<<<<<<<<<< CPF >>>>>>>>>>>>>>>>
        cpf_completo = cpf_original.zfill(11)
        elemento_cpf.send_keys(cpf_completo)
        cpf = elemento_cpf.get_attribute('value')

        # Espera explícita para o elemento dentro do segundo Shadow Root para o campo de matrícula
        elemento_matricula = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#voxel-input-1'))
        )
        matricula_original = '474147363'  # <<<<<<<<<<<<<<<<< MATRÍCULA >>>>>>>>>>>>>>>>
        matricula_completa = matricula_original.zfill(10)
        elemento_matricula.send_keys(matricula_completa)
        matricula = elemento_matricula.get_attribute('value')

        # Espera explícita para o elemento do checkbox
        elemento_checkbox = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#voxel-checkbox-1'))
        )
        elemento_checkbox.click()

        time.sleep(1)
        pyautogui.press('enter')

        # Espera explícita para o primeiro Shadow Host
        shadow_host1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > canal360i-root > canal360i-page-build > div > main > div > div > canal360i-controlador-pagina > div > div > div > canal360i-wrapper-mfe-strategy > canal360i-wrapper-mfe > div.container.ng-star-inserted > mf-corbans-chassi'))
        )
        shadow_root1 = driver.execute_script('return arguments[0].shadowRoot', shadow_host1)

        # Espera explícita para o segundo Shadow Host
        shadow_host2 = WebDriverWait(shadow_root1, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#home > div > microfrontend-corbans-chassi-base-pagina-padrao > section > div > microfrontend-corbans-chassi-inss > mf-corban-inss'))
        )
        shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', shadow_host2)

        # Espera explícita para o terceiro Shadow Host
        shadow_host3 = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#consentimento > div > componente-consentir-mfe'))
        )
        shadow_root3 = driver.execute_script('return arguments[0].shadowRoot', shadow_host3)

        # Localizar o elemento com o texto e exibir seu conteúdo
        seletor_mensagem = 'consentimento-main > componente-consentir-mfe-solicitacao-consentimento > componente-consentir-mfe-consentimento-online > div > div > voxel-alert > div > div > span'
        elemento_mensagem = WebDriverWait(shadow_root3, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor_mensagem))
        )
        texto_mensagem = elemento_mensagem.text

        # Obter o elemento para o clique dentro do terceiro Shadow Root
        link_simule_sem_consultar = WebDriverWait(shadow_root3, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#consultar-dados > div > div > p > a'))
        )

        # Usar JavaScript para clicar no elemento
        driver.execute_script("arguments[0].click();", link_simule_sem_consultar)

        # Espera explícita para o primeiro Shadow Host
        shadow_host1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > canal360i-root > canal360i-page-build > div > main > div > div > canal360i-controlador-pagina > div > div > div > canal360i-wrapper-mfe-strategy > canal360i-wrapper-mfe > div.container.ng-star-inserted > mf-corbans-chassi'))
        )
        shadow_root1 = driver.execute_script('return arguments[0].shadowRoot', shadow_host1)

        # Espera explícita para o segundo Shadow Host
        shadow_host2 = WebDriverWait(shadow_root1, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#home > div > microfrontend-corbans-chassi-base-pagina-padrao > section > div > microfrontend-corbans-chassi-inss > mf-corban-inss'))
        )
        shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', shadow_host2)

        # Localizar o elemento que contém o valor da parcela dentro do segundo Shadow Root
        valor_parcela_elemento = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#refinanciamento > div.refinanciamento-conteudo > div.refinanciamento-cabecalho > div.refinanciamento-informacoes > div:nth-child(1) > strong'))
        )
        valor_parcela = valor_parcela_elemento.text

        # Localizar o elemento que contém o número de Parcelas Pagas dentro do segundo Shadow Root
        parcelas_pagas_elemento = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#refinanciamento > div.refinanciamento-conteudo > div.refinanciamento-cabecalho > div.refinanciamento-informacoes > div:nth-child(2) > strong'))
        )
        parcelas_pagas = parcelas_pagas_elemento.text

        # Localizar o elemento que contém a Taxa Origem dentro do segundo Shadow Root
        taxa_origem_elemento = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#refinanciamento > div.refinanciamento-conteudo > div.refinanciamento-cabecalho > div.refinanciamento-informacoes > div:nth-child(3) > strong'))
        )
        taxa_origem = taxa_origem_elemento.text

        # Localizar o elemento que contém o Saldo Devedor dentro do segundo Shadow Root
        saldo_devedor_elemento = WebDriverWait(shadow_root2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#refinanciamento > div.refinanciamento-conteudo > div.refinanciamento-cabecalho > div.refinanciamento-informacoes > div:nth-child(4) > strong'))
        )
        saldo_devedor = saldo_devedor_elemento.text

        def itau_dic(cpf, matricula, valor_parcela, parcelas_pagas, taxa_origem, saldo_devedor):
            informacoes = {
                'CPF': cpf,
                'Matrícula': matricula,
                'Valor da Parcela': valor_parcela,
                'Parcelas Pagas': parcelas_pagas,
                'Taxa Origem': taxa_origem,
                'Saldo Devedor': saldo_devedor,
            }
            return informacoes
        
        itau_dic(cpf, matricula, valor_parcela, parcelas_pagas, taxa_origem, saldo_devedor)
        print(itau_dic(cpf, matricula, valor_parcela, parcelas_pagas, taxa_origem, saldo_devedor))
    
    except TimeoutException:
        print("Não foram encontrados contratos disponíveis para refinanciamento.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == '__main__':
    main()
