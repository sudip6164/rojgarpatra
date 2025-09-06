// Dashboard functionality
document.addEventListener("DOMContentLoaded", () => {
  // Initialize dashboard
  initializeDashboard()

  // Setup view toggles
  setupViewToggles()

  // Setup search functionality
  setupSearch()
})

function initializeDashboard() {
  // Add loading states
  const cards = document.querySelectorAll(".resume-card")
  cards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-2px)"
    })

    card.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0)"
    })
  })
}

function setupViewToggles() {
  const gridBtn = document.querySelector("[onclick=\"toggleView('grid')\"]")
  const listBtn = document.querySelector("[onclick=\"toggleView('list')\"]")

  if (gridBtn && listBtn) {
    gridBtn.addEventListener("click", function () {
      this.classList.add("view-toggle-active")
      listBtn.classList.remove("view-toggle-active")
    })

    listBtn.addEventListener("click", function () {
      this.classList.add("view-toggle-active")
      gridBtn.classList.remove("view-toggle-active")
    })
  }
}

function setupSearch() {
  // Add search functionality if needed
  const searchInput = document.getElementById("resume-search")
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      const query = this.value.toLowerCase()
      const resumeCards = document.querySelectorAll(".resume-card")

      resumeCards.forEach((card) => {
        const title = card.querySelector("h3").textContent.toLowerCase()
        const name = card.querySelector("p").textContent.toLowerCase()

        if (title.includes(query) || name.includes(query)) {
          card.style.display = "block"
        } else {
          card.style.display = "none"
        }
      })
    })
  }
}

// Utility functions
function showNotification(message, type = "info") {
  // Create notification element
  const notification = document.createElement("div")
  notification.className = `fixed top-4 right-4 p-4 rounded-md shadow-lg z-50 ${getNotificationClass(type)}`
  notification.textContent = message

  document.body.appendChild(notification)

  // Auto remove after 3 seconds
  setTimeout(() => {
    notification.remove()
  }, 3000)
}

function getNotificationClass(type) {
  switch (type) {
    case "success":
      return "bg-green-100 text-green-800 border border-green-300"
    case "error":
      return "bg-red-100 text-red-800 border border-red-300"
    case "warning":
      return "bg-yellow-100 text-yellow-800 border border-yellow-300"
    default:
      return "bg-blue-100 text-blue-800 border border-blue-300"
  }
}
