*** Settings ***
Library    RequestsLibrary
Library    OperatingSystem
Library    String

*** Variables ***
# ${ARQUIVO_URLS}    ${CURDIR}/lista-estados.txt
${ARQUIVO_URLS}    ${CURDIR}/rj.txt

*** Test Cases ***
Validar Lista De URLs
    ${conteudo}=    Get File    ${ARQUIVO_URLS}
    ${urls}=    Split To Lines    ${conteudo}

    FOR    ${url}    IN    @{urls}
        ${url}=    Strip String    ${url}

        IF    '${url}' != ''
            Validar URL    ${url}
        END
    END

*** Keywords ***
Validar URL
    [Arguments]    ${url}

    Log    Verificando: ${url}

    ${response}=    GET    ${url}    expected_status=any

    Log    Status: ${response.status_code}

    Should Be Equal As Integers    ${response.status_code}    200    URL inválida: ${url}