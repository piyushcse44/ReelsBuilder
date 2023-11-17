function toggleMenu() {
    const dropdown = document.getElementById('dropdown');
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
};

function togglePrices() {
    const button = document.getElementById('toggle');
    const toggle = document.getElementById('btn');
    const once = document.getElementById('once');
    const month = document.getElementById('month');
    
    if (toggle.style.float == 'left') {
        toggle.style.float = 'right';
        button.style.backgroundColor = 'var(--orange-red)';
        
        month.style.opacity = '0';
        setTimeout(() => { month.style.display = 'none'; }, 300); // Match the timeout with the transition duration

        once.style.display = 'flex'; 
        setTimeout(() => { once.style.opacity = '1'; }, 30); // Small delay to ensure the element is visible

    } else if (toggle.style.float == 'right' || !toggle.style.float) {
        toggle.style.float = 'left';
        button.style.backgroundColor = 'var(--gainsboro)';
        
        once.style.opacity = '0';
        setTimeout(() => { once.style.display = 'none'; }, 300);

        month.style.display = 'flex'; 
        setTimeout(() => { month.style.opacity = '1'; }, 30);
    }

}