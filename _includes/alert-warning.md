{% if page.show_alert %}
  > {{ page.alert_text | default: "Alerta padrão" }}
  {: .prompt-warning }
{% endif %}