-- CONFIGURAÇÃO: Defina o multiplicador de tamanho (Ex: 1.5 aumenta em 50%)
local MULTIPLICADOR = 1.5

local Players = game:GetService("Players")
local localPlayer = Players.LocalPlayer

-- Garante que o jogador e a interface existam
if localPlayer then
    local playerGui = localPlayer:WaitForChild("PlayerGui")
    
    -- Função para redimensionar o botão mantendo a proporção de Scale e Offset
    local function aumentarBotao(botao)
        if botao:IsA("TextButton") or botao:IsA("ImageButton") then
            -- Verifica se o botão já foi alterado para evitar loops
            if not botao:GetAttribute("TamanhoAlterado") then
                botao:SetAttribute("TamanhoAlterado", true)
                
                local tamanhoAtual = botao.Size
                botao.Size = UDim2.new(
                    tamanhoAtual.X.Scale * MULTIPLICADOR,
                    tamanhoAtual.X.Offset * MULTIPLICADOR,
                    tamanhoAtual.Y.Scale * MULTIPLICADOR,
                    tamanhoAtual.Y.Offset * MULTIPLICADOR
                )
            end
        end
    end

    -- Altera os botões que já existem na tela
    for _, objeto in ipairs(playerGui:GetDescendants()) do
        aumentarBotao(objeto)
    end

    -- Altera novos botões que surgirem dinamicamente (menus que abrem depois)
    playerGui.DescendantAdded:Connect(function(novoObjeto)
        aumentarBotao(novoObjeto)
    end)
    
    print("✨ Tamanho dos botões ajustado com sucesso!")
end
