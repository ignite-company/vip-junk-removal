# V.I.P. Junk Removal Production Website

Static multi-page production website built from the current GHL homepage source.

## Pages
- 1 homepage
- 9 service pages
- 3 company pages: About, Reviews, Pricing
- 8 Essex County location pages
- 404 page

## Important before launch
1. The original GHL code currently has `const FP_GHL_WEBHOOK = "";` so the homepage quiz does not post to GHL until the actual VIP webhook URL is inserted.
2. Final production domain assumed for sitemap: `https://junkremovalvip.com`. Update `sitemap.xml` and `robots.txt` if a different domain will be used.
3. Current image URLs are sourced from the existing VIP website/CDN.
4. Google Business Profile link is preserved: https://share.google/Ld9O3vo8Pq6ypLrJB

## Deployment
Use GitHub as source of truth and deploy the repository to Vercel. Keep future edits in feature branches and merge into `main` after client approval.
