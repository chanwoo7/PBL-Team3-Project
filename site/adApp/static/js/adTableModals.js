function call(){
let detailO = document.getElementsByClassName('detailO');
let editO = document.getElementsByClassName('editO');
let delO = document.getElementsByClassName('delO');

let detailC = document.getElementById('detailOk'); 
let editC = document.getElementsByClassName('editC');// 0:확인, 1:취소
let delC = document.getElementsByClassName('delC');



let detail = document.getElementById('detailContainer');
let edit = document.getElementById('editContainer');
let del = document.getElementById('delContainer');




// 각 광고 버튼 이벤트 - adId 설정
for(let i=0; i<detailO.length; i++){    
    // get_ad_details API
    
    detailO[i].addEventListener('click', () =>{
        
        detail.classList.remove('hidden');
        var adId=adIdL[i];
        
        let response;
        requestAPI2('../api/get_ad_details/'+adId+'/',"GET")
        .then(r => {console.log(r)})


    });
    editO[i].addEventListener('click', () =>{
        edit.classList.remove('hidden');
        adId=adIdL[i];
    });
    delO[i].addEventListener('click', () =>{
        del.classList.remove('hidden');
        adId=adIdL[i];
    });
}



detailC.addEventListener('click', () =>{
    detail.classList.add('hidden');
});


// edit_ad API
editC[0].addEventListener('click', () =>{
    edit.classList.add('hidden');

    alert("Edit OK!");

    let adType = document.getElementById('editAdType');
    adType = adType.options[adType.selectedIndex].text;
    let adText = document.getElementById('editAdText');
    let adUrl = document.getElementById('editAdUrl').value;
    let adFile = document.getElementById('editAdFile');
    let adName = document.getElementById('editAdTitle').value;
    let advName = document.getElementById('editAdvName').value;
    let editArray = {
        "name": adName,
        "url": adUrl,
        "text" : adText,
        "content":btoa(adFile),
        "type": adType,
        "start_time": document.getElementById('editAdStartDate').value,
        "end_time": document.getElementById('editAdEndTime').value,
        "adv_id": advName,
        "ad_price": document.getElementById('editAdPrice').value,
    };
    requestAPI('../api/edit_ad/'+adId+'/', 'PUT',editArray)
});
editC[1].addEventListener('click', () =>{
    edit.classList.add('hidden');
});



//delete_ad API
delC[0].addEventListener('click', () =>{
    
    del.classList.add('hidden');
    requestAPI('../api/delete_ad/'+adId+'/','DELETE')
    
});
delC[1].addEventListener('click', () =>{
    del.classList.add('hidden');
});




function requestAPI2(url,met,jsonArray={}){
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
}