// Main JavaScript file for RojgarPatra

// Initialize application
document.addEventListener("DOMContentLoaded", () => {
  initializeApp()
})

function initializeApp() {
  // Initialize form enhancements
  initializeForms()

  // Initialize notifications
  initializeNotifications()

  // Initialize tooltips
  initializeTooltips()

  // Initialize smooth scrolling
  initializeSmoothScrolling()

  // Initialize theme handling
  initializeTheme()
}

// Form enhancements
function initializeForms() {
  // Add loading states to forms
  const forms = document.querySelectorAll("form")
  forms.forEach((form) => {
    form.addEventListener("submit", () => {
      const submitBtn = form.querySelector('button[type="submit"]')
      if (submitBtn) {
        submitBtn.disabled = true
        submitBtn.innerHTML = '<span class="spinner"></span> Processing...'
      }
    })
  })

  // Add real-time validation
  const inputs = document.querySelectorAll("input, textarea, select")
  inputs.forEach((input) => {
    input.addEventListener("blur", validateField)
    input.addEventListener("input", clearFieldError)
  })
}

function validateField(event) {
  const field = event.target
  const value = field.value.trim()

  // Clear previous errors
  clearFieldError(event)

  // Email validation
  if (field.type === "email" && value) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(value)) {
      showFieldError(field, "Please enter a valid email address")
    }
  }

  // Required field validation
  if (field.hasAttribute("required") && !value) {
    showFieldError(field, "This field is required")
  }

  // Password strength validation
  if (field.type === "password" && field.name === "password1" && value) {
    if (value.length < 8) {
      showFieldError(field, "Password must be at least 8 characters long")
    }
  }
}

function showFieldError(field, message) {
  field.classList.add("error")

  // Remove existing error message
  const existingError = field.parentNode.querySelector(".form-error")
  if (existingError) {
    existingError.remove()
  }

  // Add new error message
  const errorDiv = document.createElement("div")
  errorDiv.className = "form-error"
  errorDiv.textContent = message
  field.parentNode.appendChild(errorDiv)
}

function clearFieldError(event) {
  const field = event.target
  field.classList.remove("error")

  const errorDiv = field.parentNode.querySelector(".form-error")
  if (errorDiv) {
    errorDiv.remove()
  }
}

// Notification system
function initializeNotifications() {
  // Auto-hide alerts after 5 seconds
  const alerts = document.querySelectorAll(".alert")
  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.opacity = "0"
      setTimeout(() => {
        alert.remove()
      }, 300)
    }, 5000)

    // Add close button
    const closeBtn = document.createElement("button")
    closeBtn.innerHTML = "×"
    closeBtn.className = "float-right text-xl font-bold cursor-pointer"
    closeBtn.onclick = () => {
      alert.style.opacity = "0"
      setTimeout(() => alert.remove(), 300)
    }
    alert.appendChild(closeBtn)
  })
}

function showNotification(message, type = "info") {
  const notification = document.createElement("div")
  notification.className = `alert alert-${type} fixed top-4 right-4 z-50 max-w-sm fade-in`
  notification.innerHTML = `
        ${message}
        <button class="float-right text-xl font-bold cursor-pointer ml-4" onclick="this.parentElement.remove()">×</button>
    `

  document.body.appendChild(notification)

  // Auto-remove after 5 seconds
  setTimeout(() => {
    notification.style.opacity = "0"
    setTimeout(() => notification.remove(), 300)
  }, 5000)
}

// Tooltip initialization
function initializeTooltips() {
  const tooltipElements = document.querySelectorAll("[data-tooltip]")
  tooltipElements.forEach((element) => {
    element.addEventListener("mouseenter", showTooltip)
    element.addEventListener("mouseleave", hideTooltip)
  })
}

function showTooltip(event) {
  const element = event.target
  const tooltipText = element.getAttribute("data-tooltip")

  const tooltip = document.createElement("div")
  tooltip.className = "tooltip"
  tooltip.textContent = tooltipText
  tooltip.style.cssText = `
        position: absolute;
        background: #333;
        color: white;
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 12px;
        z-index: 1000;
        pointer-events: none;
    `

  document.body.appendChild(tooltip)

  const rect = element.getBoundingClientRect()
  tooltip.style.left = rect.left + rect.width / 2 - tooltip.offsetWidth / 2 + "px"
  tooltip.style.top = rect.top - tooltip.offsetHeight - 8 + "px"

  element._tooltip = tooltip
}

function hideTooltip(event) {
  const element = event.target
  if (element._tooltip) {
    element._tooltip.remove()
    delete element._tooltip
  }
}

// Smooth scrolling
function initializeSmoothScrolling() {
  const links = document.querySelectorAll('a[href^="#"]')
  links.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault()
      const target = document.querySelector(this.getAttribute("href"))
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        })
      }
    })
  })
}

// Theme handling
function initializeTheme() {
  // Check for saved theme preference or default to light
  const savedTheme = localStorage.getItem("theme") || "light"
  applyTheme(savedTheme)

  // Listen for theme toggle
  const themeToggle = document.getElementById("theme-toggle")
  if (themeToggle) {
    themeToggle.addEventListener("click", toggleTheme)
  }
}

function toggleTheme() {
  const currentTheme = localStorage.getItem("theme") || "light"
  const newTheme = currentTheme === "light" ? "dark" : "light"
  applyTheme(newTheme)
  localStorage.setItem("theme", newTheme)
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme)
}

// Utility functions
function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

function throttle(func, limit) {
  let inThrottle
  return function () {
    const args = arguments
    
    if (!inThrottle) {
      func.apply(this, args)
      inThrottle = true
      setTimeout(() => (inThrottle = false), limit)
    }
  }
}

// Export functions for use in other scripts
window.RojgarPatra = {
  showNotification,
  validateField,
  showFieldError,
  clearFieldError,
  debounce,
  throttle,
}
