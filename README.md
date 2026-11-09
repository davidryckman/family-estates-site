# Family Estates website

A static, responsive public introduction to the invitation-only Family Estates app.
Support: familyestatesapp@gmail.com.

The publishable website is in `docs/`. GitHub Pages uses `main` → `/docs` in the existing repository. The new destination is `https://davidryckman.github.io/family-estates-site/`. Public deployment must be verified separately.

## Local preview

Serve `docs/` with any static HTTP server, or open `docs/index.html` directly for an offline preview. The pages require no JavaScript or build dependencies. Fonts and media are local.

## Public content

Only fictional people and sample content appear. Supplied private family screenshots are not included. The welcome image is a display-only app preview. The homepage makes no public-download or feature-availability promise beyond Coming Soon.

The privacy page remains explicitly website-only, and the account-deletion page is a contact route. Neither is an app compliance statement. Review the separate app-policy and deletion implementation work before using either for an App Store submission.

## URLs

Internal links are relative and work at either repository path. Canonical metadata, sitemap, robots and the 404 recovery links use the Family Estates destination. To set the base for a future migration:

    python scripts/set-site-url.py https://davidryckman.github.io/family-estates-site/

Run `python scripts/check-site.py` after any change. Do not rename the existing Pages repository until an old-URL redirect plan is in place: GitHub repository redirects do not guarantee redirects for a Pages site.
