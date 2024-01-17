const ADDo = document.getElementById('ADDo');
const ADTo = document.getElementById('ADTo');

const ADDc = document.getElementsByClassName('ADDc')
const ADTc = document.getElementsByClassName('ADTc')

const ADD = document.getElementById('ADDcontainer');
const ADT = document.getElementById('ADTcontainer');

ADDo.addEventListener('click', () => {
    ADD.classList.remove('hidden');
})
ADTo.addEventListener('click', () => {
    ADT.classList.remove('hidden');
})

document.getElementById('ADDok').addEventListener('click', () => {
    ADD.classList.add('hidden');
    alert();

    let adType = document.getElementById('adType');
    adType = adType.options[adType.selectedIndex].text;
    let adUrl = document.getElementById('adUrl').value;
    let adName = document.getElementById('adTitle').value;
    let advId = document.getElementById('advId').value;
    let editArray = {
        "name": adName,
        "url": adUrl,
        "type": adType,
        "start_time": document.querySelector('#adStartDate').value,
        "end_time": document.querySelector('#adEndDate').value,
        "adv_id": advId,
        "ad_price": document.getElementById('adPrice').value,
    };
    console.log(editArray)
    requestAPI('../api/add_ad/', 'POST',editArray)   

    
        
    
})
ADTc[0].addEventListener('click', () => {
    ADT.classList.add('hidden');
    
})
ADDc[1].addEventListener('click', () => {
    ADD.classList.add('hidden');
    
})
ADTc[1].addEventListener('click', () => {
    ADT.classList.add('hidden');
    
})


function requestAPI(url,met,jsonArray={}){
    const options = {
        method: met,
        headers: {
            "Content-Type": "application/json",
        },
    };
    if (met !== 'DELETE') {
        options.body = JSON.stringify(jsonArray);
    }

    fetch(url, options)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error :', error);
        });
}
