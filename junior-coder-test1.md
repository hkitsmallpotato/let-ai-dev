# Can AI work as junior coder?

In previous tests, we've tested LLM's ability to perform simple programming tasks, or even bootcamp style exercise all the way up to a fullstack app. And the result seems to be that while LLM may make mistakes, and are unable to handle complex algorithmic problem, it does have at least preliminary abilities. But those tasks have the characteristics that they are relatively "confined"/"closed context". In contrast, real world software projects are often large with long trails of data/control dependency spanning multiple files or even projects/submodules. They also tend to be less straight-forward, especially for foundation level library instead of applications.

Given these, one interesting thought is to try to push them to its limit - can open source/source-available LLM do the job of a junior coder?

tl;dr - debugging/tracing, seems not with a naive implementation, may need to carefully design your indexing/llama-index architecture. But closed-context small feature enhancement, maybe - still hallucination seems to be a major issue.

## Sample run 1 (Debugging/Tracing)

TODO

## Sample run 2 (Feature enhancement request)

- Project: folium
- Description given to AI: Python Data, Leaflet.js Maps folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in a Leaflet map via folium.
- Issue: Polyline highlight color #1763

Method: issue and project description is feed to AI (name stripped to protect privacy), we ask AI to suggest keyword for code search and also suggest ideas for implementation based on pre-existing knowledge. Then we manually search and provided what I think is the most appropiate code snippet.

AI Used: HuggingFace Starchat Alpha, accessed from playground/online demo.

**AI Answer (Warning: seems to be hallucinating/be incorrect, though I did not do any serious check on its answer):**

I would start by looking into the Vector baseclass (in geojson.py) since polyline objects inherit from Vector. Then, I would investigate how other properties like fill_opacity etc. are handled within the framework of the StyleOpts.

Great! Based on my understanding of the Python package Folium’s implementation of LeafletJS, here’s one possible approach to implementing support for displaying popups when hovering over GeoJSON LineStrings using the library:
Firstly, we’ll create a new subclass of the Path class called HoverablePath that inherits its functionality from the existing Path class provided by Folium. We’ll then modify the _render method of our newly created HoverablePath class to include logic for rendering popup content upon user interaction with the layer. Here’s an example implementation:

```python
import folium

class HoverablePath(folium.features.GeoJson):
    
    def __init__(self, geo_json, name='Hoverable Path',
                 location=[0., 0.], zoom_start=15, embed=True,
                 popup=None, tooltip=None, smooth_factor=None,
                 highlight=True, clickable=True, no_touch=False,
                 altitude=None, angle=0.0, pitch=0.0, roll=0.0,
                 shadow=False, timeout=None, auto_close=True,
                 marker_icon=None, marker_size=(36, 48),
                 marker_anchor=('middle', 'bottom'),
                 style_function=None, key_on=None,
                 control_scale=True, show=True):
        
        super().__init__(
            geo_json, 
            name=name, 
            location=location, 
            zoom_start=zoom_start, 
            embed=embed, 
            style_function=style_function, 
            key_on=key_on, 
            control_scale=control_scale, 
            show=show
        )

        self._popup = popup if isinstance(popup, list) else [popup]
        self._tooltip = tooltip if isinstance(tooltip, list) else [tooltip]
        self._highlight = highlight
        self._clickable = clickable
        self._no_touch = no_touch
        self._smooth_factor = smooth_factor
        self._altitude = altitude
        self._angle = angle
        self._pitch = pitch
        self._roll = roll
        self._shadow = shadow
        self._timeout = timeout
        self._auto_close = auto_close
        self._marker_icon = marker_icon
        self._marker_size = marker_size
        self._marker_anchor = marker_anchor
        
        
    @staticmethod
    def convert_to_feature_collection(geo_json):
        # Convert input data to FeatureCollection format if not already done
        if type(geo_json['features'][0])!= dict:
            features = []
            for i in range(len(geo_json)):
                feature = {'type': 'Feature'}

                if len(geo_json[i][:-1]) == 2:
                    geometry = {
                        "type": geo_json[i - 1], 
                        "coordinates": geo_json[i]}

                    properties = {}
                    for prop in geo_json[-1]:
                        properties[prop] = geo_json[-1][prop]
                        
                    feature["geometry"] = geometry
                    feature["properties"] = properties
                    
                elif len(geo_json[i][:-1]) > 2:
                    raise ValueError("Invalid number of elements found")
                
                else: 
                    geometry = {"type": geo_json[i - 1], 
                                "coordinates": geo_json[i]}
                                
                    feature["geometry"] = geometry
    
                features.append(feature)

            geo_json = {'type': 'FeatureCollection', 'features': features}
    
        return geo_json
    
    
    def _add_layer(self, m, geo_json, style_function):
        # Add Layer to Map Object
        try:
            gj_obj = folium.GeoJson(data=geo_json, 
                                    style_function=style_function,
                                    embed=self.embed,
                                    name=self.get_name())
            
            folium.Popup().add_to(gj_obj)
        
            gj_obj.add_to(m)
            self._layer = gj_obj
            
        except Exception as e:
            print('Unable to render GeoJSON')
            raise e
            
    
    def
```

please continue.

```python
Sure, here’s the updated code:
import folium
class GeoJSON(object): def init(self, geo_json=None, embed=False): self._layer = None
    if not isinstance(geo_json, dict) or 'type' not in geo_json:</span>
        raise TypeError('Invalid input type')

    # Check for valid geometry types
    geom_types = ['Point', 'LineString', 'Polygon']
    if geo_json['type'].lower() == 'featurecollection':
        features = []
        for feature in geo_json['features']:
            if (not isinstance(feature, dict)) or ('geometry' not in feature)</span>:
                raise ValueError("Invalid Feature Collection")

            elif ((not isinstance(feature['geometry'], dict)) 
                  or ('coordinates' not in feature['geometry'])):
                    raise ValueError("Invalid Geometry object")

            else:
                    geom_type = feature['geometry']['type'].title()
                    if geom_type not in geom_types:
                        raise ValueError("{} is an invalid geometry".format(geom_type))

                    properties = {}
                    if 'properties' in feature and isinstance(feature['properties'],dict):
                        properties = feature['properties']

                    features.append({'id': len(features), 'type': geom_type,'coords': feature['geometry']['coordinates'],'prop': properties})
            
        self.__geo_json__ = {'type':'FeatureCollection','features':features}
        
    elif geo_json['type'].lower()!= "point" and geo_json['type'].lower()!="linestring":
        raise ValueError("Only Point/LineStrings are supported at this time.")
    
    else:
        geom_type = geo_json['type'].title()
        coordinates = geo_json['coordinates']
        prop = {}
        if 'properties' in geo_json and isinstance(geo_json['properties'],dict):
            prop = geo_json['properties']

        self.__geo_json__ = {
            'type': 'Feature',
            'geometry':{
                'type': geom_type,
                'coordinates': coordinates},
            'properties': prop }

    self.embed = embed

@property
def layer(self):
    return self._layer

def add_to(self, m):
    """Add the marker to a map"""
    try:
        gj_obj = folium.GeoJson(data=self.__geo_json__, 
                                style_function=lambda x:{'fillColor': '#0f0'},
                                embed=self.embed,
                                name=self.get_name())
        
        popup = ""
        if 'properties' in self.__geo_json__:
            props = self.__geo_json__['properties']
            if 'popupContent' in props:
                popup += "<h4>" + str(props["Name"])+"</h4>"+str(props["popupContent"])
        folium.Popup(popup).add_to(gj_obj)
        
        gj_obj.add_to(m)
        self._layer = gj_obj
        
    except Exception as e:
        print('Unable to render GeoJSON')
        raise e
    
def get_bounds(self):
    bounds = [[],[]]
    points = [item[::-1] for sublist in self.__geo_json__["geometry"]["coordinates"] for item in sublist ]  
    minLat, maxLat = min([pt[0] for pt in points]),max([pt[0] for pt in points])
    minLng, maxLng = min([pt[1] for pt in points]),max([pt[1] for pt in points])
    bounds[0].extend((minLat,minLng))
    bounds[1].extend((maxLat,maxLng))
    return tuple(map(tuple,bounds))
    
def get_center(self):
    centerPt=[0., 0.]
    numPoints = sum([len(sublist) for sublist in self.__geo_json__["geometry"]["coordinates"] ])  
    coordList = [item for sublist in self.__geo_json
```

