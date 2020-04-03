document.addEventListener('DOMContentLoaded', () => {

        document.querySelector('#run').onsubmit = () => {
                
                const request = new XMLHttpRequest();
                const word = document.querySelector('#word').value;
                request.open('POST', '/runmodel');

                
                request.onload = () => {
                    const data = JSON.parse(request.responseText);
                    if(data.answer){
                        document.querySelector('#result').innerHTML = `${word} was accepted`;
                    }else{
                        document.querySelector('#result').innerHTML = `${word} was rejected`;
                    }
                }
                
        const data = new FormData();
        data.append('word', word);

        request.send(data);
        return false;
    };
        });  
