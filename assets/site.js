(() => {
  "use strict";
  const root = document.documentElement;
  root.classList.replace("no-js", "js");
  const en = root.lang === "en";
  const menu = document.querySelector("[data-menu]");
  const nav = document.querySelector("[data-nav]");
  const setMenu = (open) => {
    if (!menu || !nav) return;
    menu.setAttribute("aria-expanded", String(open));
    menu.setAttribute(
      "aria-label",
      open
        ? en
          ? "Close navigation"
          : "关闭导航"
        : en
          ? "Open navigation"
          : "打开导航",
    );
    nav.classList.toggle("open", open);
  };
  menu?.addEventListener("click", () =>
    setMenu(menu.getAttribute("aria-expanded") !== "true"),
  );
  nav?.addEventListener("click", (event) => {
    if (event.target.closest("a")) setMenu(false);
  });
  document.addEventListener("keydown", (event) => {
    if (
      event.key === "Escape" &&
      menu?.getAttribute("aria-expanded") === "true"
    ) {
      setMenu(false);
      menu.focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".header")) setMenu(false);
  });
  matchMedia("(min-width: 641px)").addEventListener("change", (event) => {
    if (event.matches) setMenu(false);
  });

  const reveal = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08 },
    );
    reveal.forEach((element) => observer.observe(element));
  } else reveal.forEach((element) => element.classList.add("visible"));

  const views = [...document.querySelectorAll("[data-view]")];
  const productImage = document.querySelector("[data-product-image]");
  const productHeading = document.querySelector("[data-product-heading]");
  const productDescription = document.querySelector(
    "[data-product-description]",
  );
  const changeView = (key) => {
    const link = views.find((view) => view.dataset.view === key) || views[0];
    if (!link || !productImage) return;
    views.forEach((view) =>
      view.setAttribute("aria-current", String(view === link)),
    );
    productImage.src = link.dataset.image;
    productImage.alt = link.dataset.alt;
    productHeading.textContent = link.dataset.heading;
    productDescription.textContent = link.dataset.description;
  };
  if (views.length) {
    changeView(new URL(location.href).searchParams.get("view") || "diet");
    views.forEach((link) =>
      link.addEventListener("click", (event) => {
        event.preventDefault();
        const url = new URL(location.href);
        url.searchParams.set("view", link.dataset.view);
        url.hash = "inside";
        history.pushState(null, "", url);
        changeView(link.dataset.view);
      }),
    );
    window.addEventListener("popstate", () =>
      changeView(new URL(location.href).searchParams.get("view") || "diet"),
    );
  }

  const search = document.querySelector("[data-faq-search]");
  const items = [...document.querySelectorAll("[data-faq]")];
  const count = document.querySelector("[data-search-count]");
  const empty = document.querySelector("[data-no-results]");
  const normalize = (text) => text.normalize("NFKC").toLocaleLowerCase().trim();
  const filterFaq = () => {
    const query = normalize(search.value);
    let matches = 0;
    items.forEach((item) => {
      const match = normalize(item.textContent).includes(query);
      item.hidden = !match;
      if (match) matches++;
    });
    if (count)
      count.textContent = query
        ? en
          ? `${matches} matching answers`
          : `找到 ${matches} 个相关回答`
        : "";
    if (empty) empty.hidden = matches > 0;
  };
  if (search) {
    search.addEventListener("input", () => {
      filterFaq();
      const url = new URL(location.href);
      if (search.value.trim()) url.searchParams.set("q", search.value.trim());
      else url.searchParams.delete("q");
      history.replaceState(null, "", url);
    });
    search.value = new URL(location.href).searchParams.get("q") || "";
    filterFaq();
    window.addEventListener("popstate", () => {
      search.value = new URL(location.href).searchParams.get("q") || "";
      filterFaq();
    });
  }
  const openHash = () => {
    const hash = location.hash.slice(1);
    const target = document.getElementById(hash);
    if (target instanceof HTMLDetailsElement) {
      target.open = true;
      target.hidden = false;
    }
  };
  openHash();
  window.addEventListener("hashchange", openHash);
  items.forEach((item) =>
    item.addEventListener("toggle", () => {
      if (!item.open) return;
      const url = new URL(location.href);
      url.hash = item.id;
      history.replaceState(null, "", url);
    }),
  );

  document.querySelectorAll("[data-copy]").forEach((button) =>
    button.addEventListener("click", async () => {
      const status = document.querySelector("[data-copy-status]");
      const value =
        button.dataset.copy === "template"
          ? document.querySelector("[data-template]").textContent
          : button.dataset.copy;
      try {
        await navigator.clipboard.writeText(value);
        if (status)
          status.textContent = en
            ? "Copied. You can paste it into your email."
            : "已复制，可以粘贴到邮件中。";
      } catch {
        if (status)
          status.textContent = en
            ? "Your browser blocked copying. Select the text below and copy it manually."
            : "浏览器未允许复制，请选中下方文字手动复制。";
      }
    }),
  );
  const print = document.querySelector("[data-print]");
  print?.addEventListener("click", () => window.print());
})();
