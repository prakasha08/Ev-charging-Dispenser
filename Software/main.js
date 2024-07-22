function updateDateTime() {
    const currentDate = new Date();
    const dateElement = document.getElementById("date");
    const timeElement = document.getElementById("time");
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    
    // Get the time in 12-hour format
    const hours = currentDate.getHours() % 12 || 12;
    const meridian = currentDate.getHours() >= 12 ? 'PM' : 'AM';
    const timeString = `${hours}:${currentDate.getMinutes().toString().padStart(2, '0')}:${currentDate.getSeconds().toString().padStart(2, '0')} ${meridian}`;
  
    dateElement.textContent = currentDate.toLocaleDateString(undefined, options);
    timeElement.textContent = timeString;
  }
  
  updateDateTime();
  
  // Update every second (1000 milliseconds)
  setInterval(updateDateTime, 1000);