function sendBot(message){
  let _0X = `
    <li class="bot">
      <div class="head">
        <small><i class='fa-solid fa-robot'></i></small>
        <p>BOT</p>
      </div>
      <div class="body">
        <p>${message}</p>
      </div>
      <div class="foot">
        <button onclick="COPY(this)"><i class="fa-solid fa-copy"></i></button>
      </div>
    </li>
  `;
  loading2();
  let ul = document.querySelector('.top');
  ul.innerHTML += _0X;
  let li = document.querySelector('article')
  li.scrollTop = li.scrollHeight;
}

function sendUser(message){
  let _09 = `
    <li class="you">
      <div class="head">
        <small><i class='fa-solid fa-user'></i></small>
        <p>YOU</p>
      </div>
      <div class="body">
        <p>${message}</p>
      </div>
    </li>
  `;
  loading2()
  let ul = document.querySelector('.top');
  ul.innerHTML += _09;
  let li = document.querySelector('article');
  li.scrollTop = li.scrollHeight;
}

function proccess(text){
  fetch(`/api/ai?model=${tite}&q=${encodeURI(text)}`)
    .then(res => res.json())
    .then(data => {
      if(data.error){
        sendBot(data.error)
      }else{
        sendBot(data.message)
      }
    })
    .catch(error => {
      sendBot(error)
    })
}

function loading1(){
  document.querySelector('.submit').innerHTML = `<i class="fa-solid fa-circle-notch fa-spin"></i>`;
}
function loading2(){
  document.querySelector('.submit').innerHTML = 'SEND';
}

function COPY(btn){
  let i = btn.parentElement;
  let o = i.parentElement.querySelector('.body p');
  alert('Copied to clipboard');
  navigator.clipboard.writeText(o.textContent);
}

function send(){
  let input = document.getElementById('inputs').value.trim();
  if(input === ''){
    return;
  }else{
    sendUser(input);
    document.getElementById('inputs').value = '';
    loading1();
    proccess(input);
  }
}