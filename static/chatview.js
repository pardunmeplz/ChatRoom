let chatCountainer = document.createElement('div')
const socket = io.connect(`${location.protocol}//127.0.0.1:5000`)
window.addEventListener('load',()=>{
    
    socket.on('connect',(msg)=>{
        const data = msg?JSON.parse(msg):[]
        renderChat(data)
    })
    socket.on('message',(msg)=>{
        const data = JSON.parse(msg)
        renderChat(data)
    })
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