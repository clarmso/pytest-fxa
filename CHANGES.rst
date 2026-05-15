Release Notes
-------------

**1.8.0b1 (2026-05-15)**

* Require PyFxA >= 0.8.2, which adds support for the ``CI_WAF_TOKEN``
  environment variable. Set ``CI_WAF_TOKEN`` in your CI environment so that
  PyFxA can send the ``fxa-ci`` header to bypass the FxA WAF / Fastly
  Dynamic Challenge once the legacy PyFxA user-agent allowlist is removed.

**1.7.0 (2026-05-15)**

* Bump PyFxA to version 0.8.1.
* Bump pyenv to version 2023.12.1.
* Test the package with Python 3.10 to 3.14. Retire support for EOL Python versions.

**1.6.0 (2024-09-27)**

* Use the official release of PyFxA 0.7.9 instead of a forked release.

**1.5.2 (2024-09-25)**

* Add maintainer and project URL.

**1.5.1 (2024-09-25)**

* Bump PyFxA (now pyfxa-mte) package so that we can remove the test account during test teardown.

**1.4.0 (2018-08-28)**

* Match session when verifying account and cleanup when verification fails.

**1.3.0 (2018-06-26)**

* Allow environment(s) to be specified using a custom ``fxa_env`` marker.

**1.2.0 (2018-06-15)**

* Catch the exception in teardown when the account has already been destroyed.

**1.1.0 (2018-05-21)**

* Provide a ``fxa_email`` fixture for accessing the email address.

* Allow users to specify the email address by passing ``--fxa-email`` command
line option or setting the ``FXA_EMAIL`` environment variable.

**1.0.0 (2018-04-12)**

* Initial release
