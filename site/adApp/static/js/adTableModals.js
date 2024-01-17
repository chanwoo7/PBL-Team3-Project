//import requestAPI from '{% static "./request.js" %}' ;
//import requestAPI from './request.js';
//import id from '{% static "./adTable.js" %}';



const detailO = document.getElementsByClassName('detailO');
const editO = document.getElementsByClassName('editO');
const delO = document.getElementsByClassName('delO');

const detailC = document.getElementsByClassName('detailC'); // 0:확인, 1:취소
const editC = document.getElementsByClassName('editC');
const delC = document.getElementsByClassName('delC');

const detail = document.getElementById('detailContainer');
const edit = document.getElementById('editContainer');
const del = document.getElementById('delContainer');


let adId=10; //값 받아와야함
for(let i=0; i<detailO.length; i++){    
    detailO[i].addEventListener('click', () =>{
        detail.classList.remove('hidden');
        //adId=id[i];
    });
    editO[i].addEventListener('click', () =>{
        edit.classList.remove('hidden');
    });
    delO[i].addEventListener('click', () =>{
        del.classList.remove('hidden');
    });
}

detailC[0].addEventListener('click', () =>{
    detail.classList.add('hidden');
});
detailC[1].addEventListener('click', () =>{
    detail.classList.add('hidden');
});
editC[0].addEventListener('click', () =>{
    edit.classList.add('hidden');
    let adType = document.getElementById('editAdType');
    adType = adType.options[adType.selectedIndex].text;
    let adUrl = document.getElementById('editAdUrl').value;
    let adName = document.getElementById('editAdTitle').value;
    let advId = document.getElementById('editAdvId').value;
    let editArray = {
        "name": adName,
        "url": adUrl,
        "type": adType,
        "start_time": document.getElementById('editAdStartDate').value,
        "end_time": document.getElementById('editAdEndTime').value,
        "adv_id": advId,
        "ad_price": document.getElementById('editAdPrice').value,
    };
    requestAPI('../api/edit_ad/'+adId+'/', 'PUT',editArray)
});
editC[1].addEventListener('click', () =>{
    edit.classList.add('hidden');
});
delC[0].addEventListener('click', () =>{
    del.classList.add('hidden');
    requestAPI('../api/delete_ad/'+adId+'/','DELETE')
    
});
delC[1].addEventListener('click', () =>{
    del.classList.add('hidden');
});

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
