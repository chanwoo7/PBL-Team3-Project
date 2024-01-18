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


//add_ad
ADDc[0].addEventListener('click', () => {
    ADD.classList.add('hidden');
    alert("ADD OK!");


    let adType = document.getElementById('adType');
    adType = adType.options[adType.selectedIndex].text;
    let adText = document.getElementById('adText').value;
    let adUrl = document.getElementById('adUrl').value;
    let adFile = document.getElementById('adFile');
    let adName = document.getElementById('adTitle').value;
    let advId = document.getElementById('advId').value;
    let addArray = {
        "name": adName,
        "url": adUrl,
        "text" : adText,
        "content":btoa(adFile), //base64인코딩
        "type": adType,
        "start_time": document.querySelector('#adStartDate').value,
        "end_time": document.querySelector('#adEndDate').value,
        "adv_id": advId,
        "ad_price": document.getElementById('adPrice').value,
    };
    console.log(addArray)
    requestAPI('../api/add_ad/', 'POST',addArray)   

    
        
    
})

//test API
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
    };

    if (met == 'POST' || met == 'PUT') {
        options.headers = {"Content-Type": "application/json",};
        options.body = JSON.stringify(jsonArray);
    }
    

    fetch(url, options)
        .then(response => response.json())
        .then(data => {
            return data;
        })
        .catch(error => {
            console.error('Error :', error);
        });
}
