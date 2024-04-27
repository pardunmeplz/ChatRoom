const sendChat = ()=>{
    const msg = document.getElementById('msgBox').value
    socket.emit('message',msg)
    document.getElementById('msgBox').value = ''
}