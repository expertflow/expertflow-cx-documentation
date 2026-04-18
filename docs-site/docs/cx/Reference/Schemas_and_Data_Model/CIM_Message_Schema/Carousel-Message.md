---
title: "Carousel Message"
summary: "CIM schema reference for the Carousel message type — used to display a slideshow or grouped set of images with associated data for interactive card-based channel experiences."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["carousel message CIM", "CIM carousel schema", "carousel message CX", "image slideshow CIM", "CIM message CAROUSEL", "card message CX", "interactive cards CIM"]
aliases: ["carousel message CIM", "CIM CAROUSEL type", "slideshow message CX"]
last-updated: 2026-03-10
---

# Carousel Message

The Carousel message is used to display a slideshow or grouped set of images — commonly used for product listing, menu options, or interactive card experiences on supported channels.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"CAROUSEL"` |
| `carouselMessageType` | Object | Yes | Carousel display configuration. See the `carouselMessageType` object reference. |
| `data` | Map | Yes | Content data for each carousel card. Each entry defines the card's display content and associated actions. |

## Notes

- Channel support for carousel rendering varies. Not all channels render carousels natively — the connector may fall back to a plain list or text representation on unsupported channels.
- The `data` map structure depends on the specific carousel layout and the actions available per card.

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Button Message](Button-Message.md)
- [Message Body](Message-Body.md)
