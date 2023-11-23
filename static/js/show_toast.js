
const Toast = {
    success(message, Settings = []) {
      this._showToast(message, 'success', Settings);
    },
    danger(message, Settings = []) {
      this._showToast(message, 'danger', Settings);
    },
    warning(message, Settings = []) {
      this._showToast(message, 'warning', Settings);
    },
    info(message, Settings = []) {
      this._showToast(message, 'info', Settings);
    },
  
    _showToast(message, type, Settings){
      let duration = Settings.duration || 3000; // Default duration in milliseconds
      let showProgress = Settings.showProgress || false;
      let toastLocation = Settings.toastLocation || 'bottom'; // top / bottom
  
      const toastContainers = {
        top: document.getElementById('shToastContainerTop'),
        bottom: document.getElementById('shToastContainerBottom'),
      };
  
      const shToastContainer = toastContainers[toastLocation];
      const toast = document.createElement('div');
      toast.classList.add('sh-toast', type);
      toast.textContent = message;
  
      const progressBar = document.createElement('div');
      progressBar.classList.add('sh-progress-bar');
  
      if(showProgress) {
        toast.classList.add('with-sh-progress-bar');
        progressBar.style.width = '0';
        toast.appendChild(progressBar);
      }
  
      shToastContainer.appendChild(toast);
      // removing previous location and then set new one
      shToastContainer.classList.remove('top', 'bottom');
      shToastContainer.classList.add(toastLocation);
  
      const startTimestamp = Date.now();
  
      function updateProgressBar() {
        const elapsedTime = Date.now() - startTimestamp;
        const remainingTime = Math.max(0, duration - elapsedTime);
        const percentage = (remainingTime / duration) * 100;
        progressBar.style.width = `${percentage}%`;
  
        if (remainingTime > 0) {
          requestAnimationFrame(updateProgressBar);
        } else {
          shToastContainer.removeChild(toast);
        }
      }
  
      requestAnimationFrame(updateProgressBar);
    }
  
  
  };
  
  
  
  
 document.addEventListener('DOMContentLoaded', function () {
    // Display a danger toast when the window is loaded
    const messageOnLoad = 'Failed to load: Incorrect credentials';
    Toast.danger(messageOnLoad, {
        showProgress: true,
    });

    // Your existing code for handling form submission and showing the toast
    document.getElementById('edit-submit-button').addEventListener('click', (e) => {
        // Prevent the default form submission

        e.preventDefault();

        // Simulate receiving a message from the backend
        const messageFromBackend = 'Login failed: Incorrect credentials';

        // Trigger the toast with the received message
        Toast.danger(messageFromBackend, {
            showProgress: true,
        });

        // You can continue with the rest of your login logic here...
        // For example, submitting the form using AJAX
        const formData = new FormData(document.getElementById('ajax-login-form'));

        fetch('user/login', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                // Handle the response as needed
                if (data.success) {
                    // Do something on success
                } else {
                    // Do something on failure
                }
            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
    });
});