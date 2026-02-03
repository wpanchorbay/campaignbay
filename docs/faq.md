# FAQ (Frequently Asked Questions)

This page contains answers to the most common questions about setting up, configuring, and troubleshooting CampaignBay.

## General Questions

### What are the minimum requirements to use CampaignBay?

To ensure the plugin runs smoothly, your website should meet the following requirements:

- WordPress Version 5.8 or higher
- PHP Version 7.0 or higher
- **WooCommerce** must be installed and activated.
- **WP-Cron** must be enabled on your server for scheduling features to work automatically.

### Will CampaignBay slow down my website?

CampaignBay has been built from the ground up with performance in mind. On your storefront, it uses a multi-level caching system to store active campaign rules. This means it only needs to query the database periodically, not on every page load, ensuring a fast experience for your customers. You can manage the cache from the **Settings → Global Settings** tab.

### Is the plugin compatible with my theme?

Yes. CampaignBay is designed to be compatible with all modern WordPress themes that follow WooCommerce standards. It fully supports both **Classic Themes** (like Storefront) and modern **Block Themes** (like Twenty Twenty-Four). We use the recommended hooks and systems to ensure that discount calculations and displays work correctly across both environments.

---

## Discount & Campaign Logic

### My discount isn't applying. What should I check first?

This is the most common issue and is usually due to a simple configuration setting. Please run through this checklist:

1.  **Is the Campaign `Active`?** Go to **CampaignBay → All Campaigns** and ensure the campaign's status toggle is set to **Active**.
2.  **Is the Schedule Correct?** If "Enable Schedule" is checked, ensure the current time is between the Start and End dates. If it is outside this range, the campaign will not apply.
3.  **Is the Product Targeted Correctly?** Double-check the "Discount Target" settings in your campaign. If it's targeted to a specific product or category, ensure the product you are testing is included in that target group.
4.  **Is "Exclude Sale Items" Enabled?** This is a campaign-level setting. Edit your campaign and check under "Other Configurations" to see if the "Exclude Sale Items" box is checked. If it is, your campaign discount will not apply to any product that already has a native WooCommerce sale price.
5.  **Is Caching Delaying the Update?** If you just created the campaign, there might be a small delay due to caching. Go to **Settings → Global Settings** and click the **"Clear Discount Cache"** button.

### Why is only one of my campaigns applying when a product qualifies for two?

This is the intended behavior by default. To prevent unexpected "double discounts," the engine first finds the single best **Product-Level** discount (`Scheduled` or `Early Bird`). This logic is controlled by the "Handle Multiple Product Discounts" setting.

If stacking is disabled, this winning discount then competes with any applicable **Cart-Level** discounts, and only the single best overall discount is applied.

::: info Learn More About This Logic
We have a dedicated guide that explains how the discount engine prioritizes and stacks different campaigns.

**[Read the Full Guide: The Discount Engine & Stacking &rarr;](./core-concepts/understanding-the-engine.md)**
:::

### Can customers use a WooCommerce coupon with a CampaignBay discount?

This is controlled by a global setting. Navigate to **Settings → Cart Settings** and toggle the **"Allow Stacking with WooCommerce Coupons"** option.

- **If OFF (Default):** The systems are mutually exclusive. If a CampaignBay discount is active, coupons cannot be applied, and vice-versa.
- **If ON:** A customer can use a coupon code on top of a price that has already been discounted by CampaignBay.

### For Quantity Discounts, is a fixed discount ($5 off) applied once or to every item?

It is applied to **every single item** that qualifies for the tier. For example, if the rule is "Buy 3 or more, get $5 off" and a customer buys 4 items, they will receive a total discount of $20 ($5 x 4).

### For Early Bird campaigns, what is counted: orders or quantity?

The system counts the number of **successful orders** (orders with a status of `processing` or `completed`). This is the fairest method and prevents a single large purchase from using up all the available Early Bird slots.

### What happens to the Early Bird count if an order is cancelled?

If an order that used an Early Bird slot is later cancelled, refunded, or fails, that "slot" is automatically **released and becomes available again**. The usage counter is decremented, ensuring the next customer can claim the offer.

---

## Frontend Display

### Can I customize the messages shown to the customer?

Yes. You have extensive control over the promotional messages displayed to your customers.

- **Product Page Messages** can be customized for each campaign type under **Settings → Product Settings**.
- **Cart Page Messages** (like the "add more to save" prompt) can be customized under **Settings → Cart Settings**.
- Most campaign types also offer a **"Discount Message Format"** field directly on the "Add/Edit Campaign" screen for even more specific control.

---

## Troubleshooting

### I updated a campaign, but the old discount is still showing. Why?

This is almost always a caching issue. Your site is temporarily showing a stored version of the active campaigns. To fix this, simply navigate to **Settings → Global Settings** and click the **"Clear Discount Cache"** button. This will force the plugin to fetch the latest rules from the database immediately.

### How do I view the plugin's debug logs?

If you are troubleshooting an issue, the debug log is the best place to start.

1.  Go to **Settings → Global Settings**.
2.  Ensure the **"Enable Debug Mode"** checkbox is checked.
3.  Click the **"View Logs"** button. This will open a modal showing the most recent events, which is invaluable for understanding how the discount engine is processing your cart.

---

## CampaignBayPro Questions

### How do I upgrade to CampaignBayPro?

Visit [wpanchorbay.com/campaignbay](https://wpanchorbay.com/campaignbay) to purchase a Pro license. After purchase, download the Pro plugin, upload it to your site, and activate your license key in **Settings → Advanced**.

### Do I need the free plugin to use CampaignBayPro?

Yes! CampaignBayPro is an extension that adds advanced features to the free CampaignBay plugin. Both must be installed and active.

### What Pro features are available?

CampaignBayPro includes:

- **BOGO Advanced (Buy X Get Y):** Create cross-sell offers with different buy and get products
- **Product In Cart Discounts:** Trigger discounts when specific products are in the cart
- **Advanced Conditions:** Target by Cart Total, Order History, Products in Cart, and more
- **Priority Email Support:** Direct access to our development team

Learn more at [wpanchorbay.com/campaignbay](https://wpanchorbay.com/campaignbay).

---

## Next Steps

Now that you've explored the FAQ, you're ready to start building your own campaigns!

- **[Create a Campaign &rarr;](./campaigns/index.md)**
- **[Back to Dashboard &rarr;](./dashboard.md)**

Need advanced features? **[Get CampaignBayPro &rarr;](https://wpanchorbay.com/campaignbay)**
