from django import template


register = template.Library()


@register.filter
def display_metadata(metadata):
    print(f'metadata is {metadata} and of type: {type(metadata)}')
    display_string = f"""
        <div><ul>
            <li>Source: {metadata['source']}</li>
            <li>Latitude: {metadata['lat']}</li>
            <li>Longitude: {metadata['lon']}</li>
            <li>Year: {metadata['year']}</li>
            <li>NREL Location ID: {metadata['location_id']}</li>
            <li>Timezone: UTC{metadata['time_zone']}</li>
            <li>Elevation: {metadata['elevation']} feet</li>
        """

    return display_string
