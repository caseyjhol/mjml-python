
0.6.0 (2021-??-??)
------------------

- support <mj-include> for body components
- mjml_to_html(): also accept plain strings as input
- add support for json-like dict as input
- avoid deprecation warnings about invalid escape sequences in regex patterns
- add support for mj-font, mj-preview and mj-raw
- better error message for unknown tags


0.5.4 (2021-01-15)
------------------

- handle <mj-head> section containing HTML comments
- also render attributes with empty values if set explicitely
- implement (basic) support for mj-class
- port "Component.allowedAttributes" from JS mjml
- ability to render "welcome-email.mjml" from "mjmlio/email-templates"


0.5.3 (2020-10-29)
------------------

- stop shipping tests in wheel
- move all requirements to setup.cfg


0.5.2 (2020-09-21)
------------------

- mjml: always return "binary" data (UTF-8) to avoid encoding problems in Windows


0.5.1 (2021-08-20)
------------------

- mjml script: use setuptools-based wrapper so Windows users can run it more easily
