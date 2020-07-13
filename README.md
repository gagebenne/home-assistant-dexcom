[![Donate](https://img.shields.io/badge/Donate-PayPal-green?style=flat-square)](https://www.paypal.me/gagebenne)
[![PyPI](https://img.shields.io/pypi/v/pydexcom?style=flat-square)](https://www.pypi.org/project/pydexcom)

*Note: this custom integration has been approved by the folks at Home Assistant, and this integration was released officially in Home Assistant .113!*

[![GitHub issue/pull request detail](https://img.shields.io/github/pulls/detail/state/home-assistant/core/33852?style=flat-square)](https://github.com/home-assistant/core/pull/33852)
[![GitHub issue/pull request detail](https://img.shields.io/github/pulls/detail/last-update/home-assistant/core/33852?style=flat-square)](https://github.com/home-assistant/core/pull/33852)
[![GitHub issue/pull request detail](https://img.shields.io/github/pulls/detail/label/home-assistant/core/33852?style=flat-square)](https://github.com/home-assistant/core/pull/33852)

# home-assistant-dexcom

The `Dexcom` integration allows you to view your CGM data from [Dexcom](https://www.dexcom.com/) in Home Assistant.

![p](https://user-images.githubusercontent.com/22921548/81246424-8d5a2780-8fe5-11ea-85f1-105a7ca6461b.png)

## Configuration

**As a custom integration, you will need to copy the `/dexcom` directory to `homeassistant/custom_components` to load it.**

You will need to set up the [Dexcom Share](https://provider.dexcom.com/education-research/cgm-education-use/videos/setting-dexcom-share-and-follow) feature in your Dexcom G6 App to use this integration. Once you have done that, perform the following steps.

**Some people have had problems with connecting when their Dexcom passwords are entirely numeric. If you have connection issues in that case, try changing your password to something with a mix of numbers and letters.**

To add `Dexcom` to your installation, go to **Configuration** >> **Integrations** in the UI, click the button with `+` sign and from the list of integrations select **Dexcom**.

#### Server

There are two Dexcom Share servers, `US` for United States customers, and `OUS` for all customers outside of the United States.

#### Unit of measurement

The integrations allows both `md/dL` and `mmol/l` units of measurement for blood glucose values. To change your preferred unit of measurement, got to **Configuration** >> **Integrations** in the UI, and click `OPTIONS`.

### Sensor

If you have a sensor session running, and once you have enabled the Dexcom integration, you should see the following sensors:

- Blood glucose value sensor
- Blood glucose trend sensor

### Example Automation

```yaml
- id: '1234567890123'
  alias: overnight_low_kitchen_lights
  description: Turn on the lights in the kitchen if my blood sugar drops low overnight
  trigger:
  - below: '65'
    entity_id: sensor.dexcom_YOUR_USERNAME_glucose_value
    platform: numeric_state
  condition: time
    after: '22:00:00'
    before: '06:00:00'
  action:
  - service: light.turn_on
      data:
        entity_id: light.kitchen
```
