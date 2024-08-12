window.addEventListener('DOMContentLoaded', (event) => {
    const personalContainer = document.querySelector('.personal-container');
    const personalItems = document.querySelectorAll('.personal-item');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const itemWidth = personalItems[0].offsetWidth + 10; // Ancho de un elemento más su margen derecho
    const itemsToShow = 3; // Cantidad de elementos a mostrar a la vez

    let currentIndex = 0;

    // Función para desplazar el carrusel hacia la izquierda
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex -= itemsToShow;
            if (currentIndex < 0) {
                currentIndex = 0;
            }
            personalContainer.scroll({
                left: currentIndex * itemWidth,
                behavior: 'smooth'
            });
        }
    });

    // Función para desplazar el carrusel hacia la derecha
    nextBtn.addEventListener('click', () => {
        const remainingItems = personalItems.length - currentIndex;
        if (remainingItems > itemsToShow) {
            currentIndex += itemsToShow;
        } else {
            currentIndex += remainingItems;
        }
        personalContainer.scroll({
            left: currentIndex * itemWidth,
            behavior: 'smooth'
        });
    });
});
