## Custom-Login
- Importieren von ```from rest_framework.authtoken.views import ObtainAuthToken```
- neue view erstellen, die von "ObtainAuthToken" erbt
- permissions festlegen
- def post(self, request) definieren. Bei Anfragen, die Daten verarbeiten muss der Request immer als Parameter angegeben werden, da er ja validiert werden soll
- in der methode wird ein serializer erstellt: ```serializer = self.serializer_class(data = request.data)```
- wenn der serializer validiert ist (```if serializer.is_valid()```) kann man die response data zusammenbauen

# 🧩 Vergleich von Django REST Framework Serializern

## Überblick

| Serializer-Typ                  | Beschreibung                                                              | Automatische Modellbindung | Geeignet für                                      | Vorteile                                                                 | Nachteile                                                          |
|--------------------------------|---------------------------------------------------------------------------|-----------------------------|---------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------|
| `serializers.Serializer`       | Manuell definierter Serializer, vergleichbar mit Django Forms             | ❌                          | Freie API-Definition, Logik außerhalb von Models  | Volle Kontrolle, unabhängig vom Modell                                   | Mehr Boilerplate, manuelle Validierung & Felder nötig             |
| `serializers.ModelSerializer`  | Automatisch generierter Serializer basierend auf einem Django-Modell      | ✅                          | CRUD für Model-basierte Daten                     | Wenig Code, enge Bindung ans Model, automatisierte Validierung           | Weniger flexibel, schwerer bei komplexer/nichtmodellierter Logik  |
| `serializers.ListSerializer`   | Für die Serialisierung ganzer Listen/Querysets                           | ✅ (als Wrapper)            | Nested Serializers, Bulk-Updates                  | Individuelle `update()`, `create()` Methoden für Listen möglich          | Muss meist zusammen mit anderem Serializer verwendet werden        |
| `serializers.HyperlinkedModelSerializer` | Wie `ModelSerializer`, aber mit URL-Referenzen statt PKs            | ✅                          | RESTful APIs mit Ressourcenverlinkung             | Saubere REST-Struktur, Links statt IDs                                   | URLs statt IDs evtl. ungewohnt; erfordert korrektes Routing        |

---

## 🛠️ Wann solltest du welchen Serializer nutzen?

| Use Case                                                 | Empfohlener Serializer                |
|----------------------------------------------------------|---------------------------------------|
| Du willst ein API-Formular unabhängig vom Modell         | `serializers.Serializer`              |
| Du willst ein einfaches CRUD für ein Django-Modell       | `serializers.ModelSerializer`         |
| Du hast verschachtelte/nestete Daten (Listen von Objekten) | `serializers.ListSerializer` (`many=True`) |
| Du möchtest REST-konforme Hyperlinks statt IDs           | `serializers.HyperlinkedModelSerializer` |

---

## 📌 Beispielunterschied: `Serializer` vs. `ModelSerializer`

```python
# Serializer
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

# ModelSerializer
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
```