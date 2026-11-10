---
name: ui-motion-performance
description: Design, review, and improve loading states, skeleton screens, interaction feedback, and UI motion in web and Android apps. Use when a product screen feels slow, flat, or janky, or when adding or refining these behaviors.
---

# UI Motion and Performance

Use this skill for real product flows, including lists, dashboards, forms, and navigation. For landing-page, portfolio, or redesign aesthetics, pair it with [design-taste-frontend](../design-taste-frontend/SKILL.md) when its scope fits.

## Pick one flow and locate the wait

Identify the screen, trigger, first visible feedback, and point where the user can continue. Separate delayed feedback, slow data or assets, and dropped frames. Reproduce the flow before editing when possible. For a review, separate measured problems from likely causes.

Inspect the existing skeletons, loading boundaries, query cache, design tokens, and animation primitives. Reuse what the app already ships. Treat product demos as visual references. Evaluate any new dependency against a concrete gap in the production app.

## Match the feedback to the state

- **First load with known layout.** Render the screen shell and available controls. If the wait is noticeable, reserve space with static skeletons that match the real row height, image ratio, and spacing. Keep placeholders out of the focus order and announce loading once where appropriate. Show content as soon as it is ready. Skip the placeholder for fast responses that would make it flash.
- **Refresh and pagination.** Keep usable content visible when it still matches the current view. Put the indicator where work is happening, such as the refresh control or the end of the list. Give empty and failed requests their own states and offer retry where appropriate.
- **Tap, save, and long-running work.** Acknowledge the input immediately. Show pending state for server-backed actions and confirm success when it arrives. Use optimistic updates for reversible actions only when rollback and failure feedback are handled. For longer tasks, show meaningful progress when it can be measured.

## Use motion to explain changes

- Give common controls a visible pressed state. For a dropdown or popover, start with a short ease-out entrance around 150-250 ms, anchored to its trigger. A slightly faster exit can work well. Treat these timings as starting points and defer to platform or design-system tokens.
- Keep sliders and dragged objects directly under the pointer or finger. Use subtle motion to connect related states or draw attention to a confirmed result. Keep the next action available as soon as its state allows it. Avoid routine bounce, long cascades, and repeated shimmer by default.
- Preserve state and feedback with motion reduced or disabled. On web, honor `prefers-reduced-motion` and favor `transform` and `opacity` for simple animation. On Android, respect the platform animation setting and use the app's existing native or cross-platform motion primitives.

## Verify the change

Compare time to first visible feedback and time to first usable content before and after under comparable conditions. Check first load, fast responses, refresh, empty and error paths, and reduced motion as applicable. Check for layout shifts on web and slow frames on a physical Android device with a release build when available. Exercise the flow under a slower connection. If the real wait remains high, inspect the request, payload, or render trace before choosing a fix. A skeleton can improve the experience during a wait. Claim a speedup only when the measurement supports it.

[Web Vitals](https://web.dev/articles/vitals) | [Web animation performance](https://web.dev/articles/animations-guide) | [Android Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
