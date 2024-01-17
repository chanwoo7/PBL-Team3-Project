const ADDo = document.getElementById('ADDo');
const ADTo = document.getElementById('ADTo');

const ADDc = document.getElementsByClassName('ADDc')//객체배열
const ADTc = document.getElementsByClassName('ADTc')

const ADD = document.getElementById('ADDcontainer');
const ADT = document.getElementById('ADTcontainer');

ADDo.addEventListener('click', () => {
    ADD.classList.remove('hidden');
    
})
ADTo.addEventListener('click', () => {
    ADT.classList.remove('hidden');
})

ADDc[0].addEventListener('click', () => {
    ADD.classList.add('hidden');
    
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