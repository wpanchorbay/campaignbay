# Changelog

What changed in each release, in plain language. Free = CampaignBay (WordPress.org). Pro = CampaignBayPro.

::: info Updating?
Update **Free first**, then Pro. Pro 1.1.0 requires Free 1.1.13 or later. See [Upgrading](./installation.md#upgrading).
:::

## CampaignBay Free 1.2.0

### New

- Countdown timers on product, shop and cart pages, and anywhere with a shortcode.
- A CampaignBay sale badge, category/shop offer messages and campaign promo blurbs.
- Quantity-tier labels and a cards layout for the discount table.
- A fixed quantity discount can apply **per item** or **once to the whole line**.
- Per-campaign minimum, maximum and step quantity limits.
- Product tag targeting, plus "guest vs logged-in" and "cart item quantity" conditions.
- A "Most recently started wins" priority method.
- Dashboard date ranges for 90 days, 1 year and a custom range.

### Improved

- Product and cart prices now respect your "prices entered with/without tax" and display-tax settings for quantity and fixed-price discounts.
- Importing a campaign keeps its usage count and only expires it when the limit is truly reached. Cancelling an order re-activates a campaign that expired from its usage limit.
- Duplicating a campaign now keeps its conditions.
- Cart-total conditions refresh correctly when shipping changes.
- New filters for developers and Pro to extend coupons, cart conditions and tier-required campaign types.

### Fixed

- A usage limit of N now expires the campaign after N orders, not N-1.
- Early Bird tiers whose uses are spent no longer give a discount, warnings, a sale badge or a countdown.
- Variable product price ranges now show the true minimum and maximum.
- Fee-mode quantity discounts on tax-inclusive stores; empty and zero dates; tag lookup and tag names when reopening a campaign; the block checkout countdown.
- Conditions on product-level rules are now honoured in the cart.
- The "show quantity table" setting is tied to the right option.
- Ordinary coupons are removed from the classic cart when stacking is off, and stale CampaignBay coupons are removed after a campaign changes.
- The "Sale!" badge no longer shows when a fixed-price campaign leaves the price at or above the regular price.
- Quantity and Fixed Price campaigns can no longer be saved without tiers.
- Campaign fields now validate as true booleans and strings. **REST clients must send real booleans** (`true`/`false`, `1`/`0`), not values like `"yes"`.
- Campaign labels on the cart discount line are escaped (security hardening).
- A deleted product in the cart no longer causes a PHP error, and importing campaigns with array fields no longer returns a server error.
- Removed PHP warnings on partial REST requests and a dashboard chart warning.
- The filtered admin script URL for the legacy build is now the one that loads.

## CampaignBayPro 1.1.0

Requires CampaignBay Free 1.1.13 or later.

### New

- 10 new campaign types: [Fixed Price](./campaigns/fixed-price-discounts.md), [Variation](./campaigns/variation-discounts.md), [Cheapest Item](./campaigns/cheapest-item-discounts.md), [Weight](./campaigns/weight-discounts.md), [Bulk Sum](./campaigns/bulk-sum-discounts.md), [Bundle](./campaigns/bundle-discounts.md), [Auto-add / Recommended Product](./campaigns/auto-add-recommended-product.md), [Free Gift](./campaigns/free-gift.md), [Category BOGO](./campaigns/category-bogo.md) and [Nth Unit](./campaigns/nth-unit-discounts.md).
- New [conditions](./core-concepts/pro-conditions.md): activation by coupon code or link; order history (first order, order count, lifetime spend, previous product) with a per-customer limit; day and time; product stock; product attribute; email domain; payment method; shipping method; shipping zone; cart weight.
- An [Offer type messages](./settings/offer-messages.md) settings card for shopper messages.

### Improved

- The Pro campaign editor now matches Free 1.2.0: countdown, promote, quantity limits, fixed discount basis, tier labels and the new settings sections. Unknown settings are no longer wiped when you save.

### Fixed

- Product In Cart discounts now honour the "line total" and "fee" apply-as choices, with a matching editor option.
- BOGO Advanced is restored: free items are added as their own flagged cart line, with the repeat setting, stock cap, usage counting and cart messages.
- BOGO Advanced in manual mode no longer counts a unit as both a buy unit and the free reward, or uses units already discounted by another offer.
- Security hardening of labels, cookies and offer calculations.

## Earlier versions

**Free 1.1.x**

- 1.1.12: scheduled campaigns without a start date activate immediately; open-ended quantity tiers apply at checkout; bulk delete handles already-deleted campaigns.
- 1.1.11: storefront crash fixes for category-targeted and BOGO campaigns; partial updates no longer wipe tiers or targets; license key masked in the admin and REST responses.
- 1.1.8: optional deactivation feedback and a dismissible review reminder.
- 1.1.7: Cart Total conditions.
- 1.1.2: Campaign Calendar page and dashboard calendar widget.
- 1.1.0: complete admin redesign and multi-select campaign filters.

**Free 1.0.x**

- 1.0.8: campaign templates (Flash Sale, BOGO, Bulk Discount, Early Bird).
- 1.0.7: Conditions with user role targeting.
- 1.0.6: options to turn off promotional messages on cart and product pages.
- 1.0.5: BOGO free products added as separate cart lines.
- 1.0.2: interactive tour guide.
- 1.0.0: initial release.

**Pro 1.0.x**

- 1.0.3: license key masked; unrelated settings can no longer overwrite it.
- 1.0.2: Cart Total conditions.
- 1.0.0: initial release with BOGO Advanced, Product In Cart, advanced conditions and license activation.
