---
layout: home

hero:
  name: "CampaignBay"
  text: "The Ultimate Discount Campaign Manager for WooCommerce."
  tagline: Create powerful, automated, and targeted discount campaigns to drive sales and engage your customers.
  image:
    src: /dashboard-overview.png
    alt: CampaignBay Dashboard
  actions:
    - theme: brand
      text: Get Started
      link: /installation
    - theme: alt
      text: Buy Pro
      link: https://wpanchorbay.com/campaignbay
    - theme: alt
      text: Free Download
      link: https://wordpress.org/plugins/campaignbay/
---

## What is CampaignBay?

Welcome to the official documentation for CampaignBay!

CampaignBay is a powerful, user-friendly marketing tool that empowers you to create sophisticated, automated discount campaigns directly from your WordPress dashboard. Whether you're running a Black Friday flash sale, rewarding customers for bulk purchases, or creating urgency with a limited-time offer, CampaignBay provides the robust features you need to drive sales and engage customers.

With its intuitive dashboard, flexible campaign types, and high-performance discount engine, you get unparalleled control over your marketing strategy without sacrificing site speed.

This documentation will guide you through every feature, from installing the plugin to understanding the advanced settings.

## Key Features

**Campaign Types:**

- **Scheduled Discounts:** Run time-limited sales with automatic start and end dates. Perfect for holiday sales or weekly specials.
- **Quantity Based Discounts:** Tiered pricing like "Buy 3+, get 10% off; Buy 5+, get 20% off." Customers see a pricing table on the product page.
- **Early Bird Discounts:** Reward the first X customers with special pricing. A live counter shows remaining slots.
- **BOGO (Buy One Get One):** Classic "Buy 2, Get 1 Free" or "Buy 1, Get 1 at 50% Off" deals. Free items are added directly to the cart.

See the [full list of Free and Pro campaign types](/campaigns/#free-vs-pro-campaign-types).

**Targeting & Conditions:**

- **Flexible Targeting:** Apply discounts to your entire store, specific products, categories, or product tags.
- **Product & Category Exclusions:** Fine-tune which items are excluded from discounts.
- **Conditions:** Restrict campaigns by user role, guest vs logged-in, cart total, or cart item quantity.
- **Smart Stacking Logic:** Control how discounts interact with each other and native WooCommerce coupons.
- **Coupon Compatibility:** Works seamlessly with WooCommerce coupons (configurable stacking).

**Display & Messaging:**

- **Countdown Timers:** Show a live countdown on product, shop and cart pages, or anywhere with a shortcode.
- **Sale Badge & Offer Messages:** A CampaignBay sale badge, category/shop offer messages and campaign promo blurbs.
- **Quantity Limits:** Set a minimum, maximum and step quantity per campaign.
- **Customizable Messages:** Dynamic placeholders like `{percentage_off}`, `{buy_quantity}` for promotional text.
- **Product Page Display:** Discount tables and banners automatically appear on product pages.
- **Cart Integration:** Automatic discounts with strikethrough pricing in the cart.
- **Campaign Templates:** Pre-built templates for quick campaign setup.

**Analytics Dashboard:**

- **KPI Cards:** Active Campaigns, Total Discount Value, Discounted Orders, Sales from Campaigns.
- **Interactive Charts:** Line, bar, and pie chart visualizations for discount trends.
- **Top Performing Campaigns:** Identify your best campaigns at a glance.
- **Recent Activity Log:** Track campaign creation and updates.
- **Live & Upcoming Campaigns:** Quick view of active and scheduled promotions.

**Performance & Automation:**

- **Full Scheduling & Automation:** Reliable WP-Cron based activation/deactivation with failsafe mechanisms.
- **Performance Optimized:** Multi-level caching keeps your storefront blazingly fast.
- **100% Free Core Features:** No artificial limits. Create unlimited campaigns.

## Pro Features

Unlock advanced capabilities with [**CampaignBayPro**](https://wpanchorbay.com/campaignbay). Pro 1.1.0 adds these campaign types:

- **[Fixed Price](/campaigns/fixed-price-discounts):** Sell a product, or a quantity of it, at an exact price.
- **[Variation Discounts](/campaigns/variation-discounts):** Discount specific variations of variable products.
- **[Cheapest Item](/campaigns/cheapest-item-discounts):** Discount the cheapest item(s) in a group, like "buy 3, cheapest is free".
- **[Weight Discounts](/campaigns/weight-discounts):** Reward heavier or lighter carts by total weight.
- **[Bulk Sum](/campaigns/bulk-sum-discounts):** Tiered discounts based on the combined quantity of a group of products.
- **[Bundle Discounts](/campaigns/bundle-discounts):** Discount when customers buy a set of products together.
- **[Auto-add / Recommended Product](/campaigns/auto-add-recommended-product):** Automatically add, or recommend, a product when conditions are met.
- **[Free Gift](/campaigns/free-gift):** Give a free product when the cart qualifies.
- **[Category BOGO](/campaigns/category-bogo):** Buy from one category, get items from another.
- **[Nth Unit](/campaigns/nth-unit-discounts):** Discount every 2nd, 3rd or Nth unit.
- **[BOGO Advanced](/campaigns/bogo-advanced-discounts)** and **[Product In Cart](/campaigns/product-in-cart-discounts):** Cross-sell offers and cart-triggered discounts.
- **[Advanced Conditions](/core-concepts/pro-conditions):** Coupon code or link activation, order history, day and time, stock, product attribute, email domain, payment method, shipping method and zone, cart weight, and more.
- **[Offer Messages](/settings/offer-messages):** Shopper messages for each Pro offer type.
- **Priority Email Support:** Get direct access to our development team.

[**Get CampaignBayPro →**](https://wpanchorbay.com/campaignbay)

## Live Demo

Experience the power of CampaignBay firsthand on our interactive demo site. See how campaigns look on the frontend and explore the admin dashboard.

- [**View the Demo (Frontend & Backend)**](https://wpanchorbay.com/campaignbay/#demo)

## Use Cases

CampaignBay is designed to help you achieve specific business goals. Here are just a few examples of what you can build:

- **Launch New Products with a Bang:** Create an **Early Bird Discount** offering a steep discount to the first 50 customers to generate instant buzz and social proof.

- **Increase Average Order Value (AOV):** Implement a tiered **Quantity Discount** like "Buy 3+, get 10% off; Buy 5+, get 20% off" and use the built-in cart notices to encourage customers to add more to their cart.

- **Run Holiday Flash Sales:** Set up a **Scheduled Discount** for your entire store that automatically starts at midnight on Black Friday and ends precisely on Cyber Monday.

- **Clear Out Old Inventory:** Run a "Buy 2, Get 1 Free" **BOGO Campaign** on last season's styles to quickly move stock without devaluing your brand.

- **Create Simple Wholesale Tiers:** Use **Quantity Discounts** on specific product categories to offer wholesale-style pricing to all your customers without needing a separate plugin.

- **Targeted Promotions:** Apply a discount to a specific product category to promote a new line or run a brand-specific sale.

- **Cross-Sell Bundles (Pro):** With [CampaignBayPro](https://wpanchorbay.com/campaignbay), trigger discounts on accessories when customers add specific products to their cart.

## Getting Started

Ready to dive in? Here are the most important sections to get you started on your journey.

<div class="vp-doc">
  <div class="vp-card-group">
    <div class="vp-card">
      <a href="./installation">
        <h3>1. Installation</h3>
        <p>A step-by-step guide to installing and activating the plugin on your WordPress site.</p>
      </a>
    </div>
    <div class="vp-card">
      <a href="./campaigns/scheduled-discounts">
        <h3>2. Creating Your First Campaign</h3>
        <p>Learn the basics by creating a simple, time-based scheduled discount.</p>
      </a>
    </div>
    <div class="vp-card">
      <a href="./settings">
        <h3>3. Configuring Settings</h3>
        <p>Explore the global settings to tailor the plugin's behavior to your store's strategy.</p>
      </a>
    </div>
  </div>
</div>
