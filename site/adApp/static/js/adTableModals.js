const detailO = document.getElementsByClassName('detailO');
const editO = document.getElementsByClassName('editO');
const delO = document.getElementsByClassName('delO');

const detailC = document.getElementsByClassName('detailC');
const editC = document.getElementsByClassName('editC');
const delC = document.getElementsByClassName('delC');

const detail = document.getElementById('detailContainer');
const edit = document.getElementById('editContainer');
const del = document.getElementById('delContainer');
console.log(detailC)
for(let i=0; i<detailO.length; i++){
    detailO[i].addEventListener('click', () =>{
        detail.classList.remove('hidden');
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
});
editC[1].addEventListener('click', () =>{
    edit.classList.add('hidden');
});
delC[0].addEventListener('click', () =>{
    del.classList.add('hidden');
});
delC[1].addEventListener('click', () =>{
    del.classList.add('hidden');
});
