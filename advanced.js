// Christmas Sunday Finder Function
function findXmasSunday(startYear, endYear) {
  const sundayYears = [];

  for (let year = startYear; year <= endYear; year++) {
    const xmasDate = new Date(year, 11, 25);
    if (xmasDate.getDay() === 0) {
      sundayYears.push(year);
    }
  }

  return sundayYears;
}

// Advanced JavaScript Features
class ChristmasSundayFinder {
  constructor() {
    this.currentYear = new Date().getFullYear();
    this.initializeSnow();
    this.setupEventListeners();
    this.validateInputs();
  }

  initializeSnow() {
    const snowContainer = document.getElementById("snowContainer");
    const snowflakes = ["❄", "❅", "❆"];

    for (let i = 0; i < 50; i++) {
      const snowflake = document.createElement("div");
      snowflake.className = "snowflake";
      snowflake.innerHTML =
        snowflakes[Math.floor(Math.random() * snowflakes.length)];
      snowflake.style.left = Math.random() * 100 + "%";
      snowflake.style.animationDuration = Math.random() * 3 + 2 + "s";
      snowflake.style.animationDelay = Math.random() * 2 + "s";
      snowflake.style.fontSize = Math.random() * 10 + 10 + "px";
      snowflake.style.opacity = Math.random() * 0.7 + 0.3;
      snowContainer.appendChild(snowflake);
    }
  }

  setupEventListeners() {
    const startYear = document.getElementById("startYear");
    const endYear = document.getElementById("endYear");

    startYear.addEventListener("input", () => this.validateInputs());
    endYear.addEventListener("input", () => this.validateInputs());

    // Add enter key support
    [startYear, endYear].forEach((input) => {
      input.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
          findXmasSundays();
        }
      });
    });
  }

  validateInputs() {
    const startYear = document.getElementById("startYear");
    const endYear = document.getElementById("endYear");
    const startValue = parseInt(startYear.value);
    const endValue = parseInt(endYear.value);

    if (startValue && endValue && startValue > endValue) {
      startYear.style.borderColor = "red";
      endYear.style.borderColor = "red";
      return false;
    } else {
      startYear.style.borderColor = "var(--primary-green)";
      endYear.style.borderColor = "var(--primary-green)";
      return true;
    }
  }

  calculateStatistics(years, startYear, endYear) {
    const totalYears = endYear - startYear + 1;
    const frequency = ((years.length / totalYears) * 100).toFixed(1);

    // Find next Sunday Christmas
    const nextSunday =
      years.find((year) => year >= this.currentYear) || "None in range";

    // Calculate average gap
    let gaps = [];
    for (let i = 1; i < years.length; i++) {
      gaps.push(years[i] - years[i - 1]);
    }
    const avgGap =
      gaps.length > 0
        ? (gaps.reduce((a, b) => a + b, 0) / gaps.length).toFixed(1)
        : "-";

    return {
      total: years.length,
      frequency: frequency,
      next: nextSunday,
      gap: avgGap
    };
  }
}

// Global functions
function findXmasSundays() {
  const startYear = parseInt(document.getElementById("startYear").value);
  const endYear = parseInt(document.getElementById("endYear").value);

  if (!startYear || !endYear) {
    alert("Please enter both start and end years!");
    return;
  }

  if (startYear > endYear) {
    alert("Start year must be less than or equal to end year!");
    return;
  }

  if (startYear < 1900 || endYear > 3000) {
    alert("Please enter years between 1900 and 3000!");
    return;
  }

  // Show loading
  document.getElementById("loading").style.display = "block";
  document.getElementById("resultsSection").style.display = "none";

  // Simulate processing time for better UX
  setTimeout(() => {
    const years = findXmasSunday(startYear, endYear);

    // Hide loading
    document.getElementById("loading").style.display = "none";

    // Display results
    displayResults(years, startYear, endYear);
  }, 500);
}

function displayResults(years, startYear, endYear) {
  const resultsSection = document.getElementById("resultsSection");
  const resultsCount = document.getElementById("resultsCount");
  const yearsGrid = document.getElementById("yearsGrid");

  // Clear previous results
  yearsGrid.innerHTML = "";

  // Update count
  resultsCount.textContent = `Found ${years.length} years where Christmas falls on Sunday`;

  // Create year items with animation
  years.forEach((year, index) => {
    setTimeout(() => {
      const yearItem = document.createElement("div");
      yearItem.className = "year-item";
      yearItem.textContent = year;
      yearItem.onclick = () => showYearDetails(year);
      yearItem.style.animation = "fadeIn 0.5s ease-out";
      yearsGrid.appendChild(yearItem);
    }, index * 50);
  });

  // Calculate and display statistics
  const finder = new ChristmasSundayFinder();
  const stats = finder.calculateStatistics(years, startYear, endYear);

  document.getElementById("totalYears").textContent = stats.total;
  document.getElementById("frequency").textContent = stats.frequency + "%";
  document.getElementById("nextSunday").textContent = stats.next;
  document.getElementById("gap").textContent = stats.gap;

  // Show results
  resultsSection.style.display = "block";
}

function showYearDetails(year) {
  const date = new Date(year, 11, 25);
  const dayName = date.toLocaleDateString("en-US", { weekday: "long" });
  const dateString = date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric"
  });

  alert(`December 25th, ${year} falls on ${dayName}\n\nDate: ${dateString}`);
}

function clearResults() {
  document.getElementById("resultsSection").style.display = "none";
  document.getElementById("startYear").value = "";
  document.getElementById("endYear").value = "";
}

function loadExample() {
  document.getElementById("startYear").value = "2000";
  document.getElementById("endYear").value = "2100";
  findXmasSundays();
}

// Initialize the application
document.addEventListener("DOMContentLoaded", () => {
  new ChristmasSundayFinder();

  // Set default years
  document.getElementById("startYear").placeholder = "2000";
  document.getElementById("endYear").placeholder = "2100";
});

// Add some Easter eggs
let clickCount = 0;
document.querySelector(".title").addEventListener("click", () => {
  clickCount++;
  if (clickCount === 5) {
    alert("🎅 Ho ho ho! Merry Christmas! 🎄");
    clickCount = 0;
  }
});
