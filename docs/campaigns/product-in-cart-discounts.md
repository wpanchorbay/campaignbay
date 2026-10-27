# Campaign Type: Product In Cart

::: tip Pro Feature
This is a **CampaignBayPro** feature. [Upgrade to Pro](https://wpanchorbay.com/campaignbay) to unlock Product In Cart discounts and other powerful features.
:::

The **Product In Cart** campaign is a conditional discount type. It allows you to offer a discount on specific items (or the entire cart) _only if_ a particular "trigger product" is present in the customer's cart.

This is ideal for membership-style perks or "lock and key" offers:

- "Buy this **Membership Card** and get **10% off everything** else."
- "Add a **Gift Box** to your cart to get **$5 off** your jewelry purchase."

## Step 1: Select Your Campaign Type

To begin, navigate to **CampaignBay → Add Campaign**.

![Select Campaign Type](./../public/product-in-cart-selection.png)

- **Select Discount Type:** Choose **`Product In Cart`** from the list. This unlocks the conditional logic fields for trigger-based discounts.

![Campaign Title](./../public/common-campaign-title.png)

- **Campaign Title:** Give your campaign a clear and descriptive name (e.g., "VIP Membership Perk").

![Save Actions](./../public/common-save-actions.png)

- **Select Status:**
  - **Active:** The campaign will be live immediately (or on its scheduled start time).
  - **Inactive:** Save the campaign as a draft.

## Step 2: Define the Conditions & Discount

This campaign relies on a simple "If This, Then That" logic. You define which product triggers the discount and how that discount is applied.

![Trigger and Discount Empty](./../public/product-in-cart-condition-empty.png)

### 1. The Trigger (If product...)

Select the **trigger product**. This is the item that must be in the customer's cart for the discount to activate.

![Trigger Product](./../public/product-in-cart-trigger-product.png)

- **Select a Product:** Search for and select the item (e.g., "VIP Membership").

### 2. The Discount (Apply...)

Enter the numeric **value** of the discount and choose the **Discount Type**:

![Discount Type Options](./../public/product-in-cart-discount-type-options.png)

- **Percentage Discount (%):** A percentage off the target items.
- **Fixed Discount on Cart Total:** A fixed amount off the total subtotal of the target items.
- **Fixed Discount Per Item:** A fixed amount off **every** individual target item in the cart.

### 3. The Target (Apply discount on...)

Choose which products are eligible for the discount once the trigger item is added:

![Apply On Options](./../public/product-in-cart-apply-on-options.png)

- **Entire Store:** Every other item in the cart gets the discount.
- **Specific Products:** Only specific items or categories you choose will be discounted.

![Specific Product Selection](./../public/product-in-cart-apply-on-specific.png)

If you chose **Specific Products**, search for and select the eligible items in the secondary dropdown.

### 4. Show the discount as

::: tip New in Pro 1.1.0
Choose how the discount is presented in the cart. The total the shopper pays is the same in all three; only the presentation differs.
:::

![The Show the discount as selector open with its three options](./../public/product-in-cart-show-discount-as.png)

- **A coupon line in the cart totals** (default): the discount appears like a coupon in the cart totals, with a **[Remove]** link.
- **A lower price on the item:** the target item's price is reduced and shown crossed out in the cart and mini-cart.
- **A separate discount line in the cart totals:** the item keeps its price and one negative line, named after the campaign, appears in the totals. It has no Remove link, and there is one line per campaign (all target lines combined).

Example: trigger product E (25.00) and target A (100.00) at 10%, cart E ×1 and A ×2.

| Show the discount as | What the cart shows | Total |
| --- | --- | --- |
| A coupon line in the cart totals | A 100.00 each; a coupon row −20.00; subtotal 225.00 | 205.00 |
| A lower price on the item | A 90.00 each (line 180.00); subtotal 205.00 | 205.00 |
| A separate discount line in the cart totals | A 100.00 each; a campaign line −20.00 | 205.00 |

"A lower price on the item" never changes the price on the product page or in the shop. A **Fixed Discount Per Item** takes the amount or the item's price, whichever is smaller, off each unit. A **Fixed Discount on Cart Total** is split across the target lines in proportion to their value and never exceeds their total.

## Step 3: Set Conditions (Optional)

You can add specific rules to restrict who can use this discount.

![Conditions Overview](./../public/product-in-cart-conditions-overview.png)

**[Read the Full Guide: How to Use Conditions &rarr;](../core-concepts/conditions.md)**

## Step 4: Set Other Configurations (Optional)

This section provides additional rules for your campaign.

![Exclude Sale Item](./../public/product-in-cart-sidebar-exclude-sale-item.png)

- **Exclude Sale Items:** Check this box if you do not want this campaign's discount to apply to products that are already on sale in WooCommerce. This is useful for preventing "double discounting."

![Enable Usage Limit](./../public/product-in-cart-sidebar-usage-limit.png)

- **Enable Usage Limit:** Check this box to set a maximum number of times this campaign can be used across your entire store. Once the limit is reached, the campaign will automatically become inactive.

## Step 5: Set the Schedule (Optional)

You can optionally schedule your campaign to run during a specific time window. This section controls when your campaign will automatically start and end.

![Enable Schedule](./../public/product-in-cart-sidebar-schedule-dates.png)

- **Start Time / End Time:** Use the date and time pickers to set the exact moment for the campaign to activate and expire.

::: tip Timezone Information
All dates and times are based on the timezone you have configured in your main WordPress settings under **Settings → General → Timezone**. The system automatically handles all UTC conversions for you.
:::

::: info Learn More About Automation
The status of your campaign is closely tied to the scheduling system, which uses WordPress Cron to automate activation and expiration.

**[Read the Full Guide: Scheduling & Automation &rarr;](../core-concepts/scheduling-and-automation.md)**
:::

## Step 6: Define Display Configurations

![Show Promo Message](./../public/product-in-cart-show-message.png)

- **Show Product Page Message:** Toggle this to enable or disable the custom message on the target product pages.

![Product Page Message](./../public/product-in-cart-message-format.png)

- **Product Page Message Format:** Customize the text using placeholders like `{campaign_title}` and `{discount_value}`.
  - _Example:_ `{campaign_title} offer: Buy the VIP Pass and get {discount_value}% off this item!`

- **Cart Page Discount Message Format:** Enter a message to display on the cart page when the discount is applied.
- **Cart Page Message Location:** Choose where the cart message should appear.

## Step 7: Save the Campaign

Once you have configured all the options, click the **Save Campaign** button. You will be redirected to the "All Campaigns" list.

You have now learned about all campaign types. It's time to explore the global settings that control your entire discount system.

- **[Configuring the Settings &rarr;](../settings/index.md)**
