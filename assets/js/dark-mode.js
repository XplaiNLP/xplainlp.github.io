document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("dark-mode-toggle");
    const currentTheme = localStorage.getItem("theme");

    if (currentTheme) {
        document.documentElement.setAttribute("data-theme", currentTheme);
    } else if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
        document.documentElement.setAttribute("data-theme", "dark");
    }

    toggle.addEventListener("click", function () {
        let newTheme = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);
    });
});
