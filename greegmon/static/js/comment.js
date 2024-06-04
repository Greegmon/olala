async function execute(){
  try{
    let post = document.getElementById('post-id');
    let token = document.getElementById('token');
    let message = document.getElementById('comment');
    let count = document.getElementById('count');
    let div = document.getElementById('output');
    div.innerHTML = "<p>Sending....</p>";
    const api = await fetch(`/api/auto-comment?postId=${post.value}&token=${token.value}&comment=${message.value}&count=${count.value}`)
    const data = await api.json();
    if(data.status === 'error'){
      div.innerHTML = `<p>Somthing went wrong.</p>`;
    }else{
      div.innerHTML = `<p class='ok'>Total Comment: ${data.total}</p>`;
    }
  }catch(error){
    div.innerHTML = `<p>${error}</p>`;
    console.log(error)
    Swal.fire({
      icon: 'error',
      text: error
    })
  }
}