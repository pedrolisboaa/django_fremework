document.getElementById('btn-cpf').addEventListener('submit', function(evento){
    let cpfInput = document.getElementById('btn-cpf')
    let limpandoCpf = cpfInput.value.replace(/[.-]/g, '')
    cpfInput.value = limpandoCpf
})

console.log('oi!')