let chatCountainer = document.createElement('div')

window.addEventListener('load',()=>{
    renderChat(['heyya','wasssssup','newgamme'])
})

const renderChat = (data)=>{
    const element = document.getElementById("chatView")
    if (element.children.length>0)element.removeChild(chatCountainer)
    chatCountainer = document.createElement('div')
    chatCountainer.classList.add('chatContainer')
    for(msg of data){
        const item = document.createElement('span')
        item.innerHTML = msg
        chatCountainer.appendChild(item)
    }
    element.appendChild(chatCountainer)
}