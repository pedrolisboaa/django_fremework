// Busco os elementos do javascript e converso para float
let celulasDePreco = document.querySelectorAll('#preco')
let celulasDeEstoque = document.querySelectorAll('#estoque')
let celulasDeValor = document.querySelectorAll('#valor')

for(let i = 0; i < celulasDePreco.length; i++){
    let preco = parseFloat(celulasDePreco[i].textContent).toFixed(2)
    console.log(preco)
    let estoque = parseFloat(celulasDeEstoque[i].textContent)

    let calculoEstoque = (preco * estoque).toString()
    celulasDeValor[i].textContent = calculoEstoque
}


