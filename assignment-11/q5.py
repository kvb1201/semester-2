# Given a dataset of concerts, count the number of concerts per (artist, venue), per year
# month. Make the resulting table be a wide table - one row per year month with a column
# for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
# to determine which (artist, venue) pairs to include in the result.

import pandas as pd

# Sample concert data
concerts_data = {
    'date': [
        '2024-01-05', '2024-01-10', '2024-01-15',
        '2024-02-03', '2024-02-10', '2024-02-20',
        '2024-03-01'
    ],
    'artist': [
        'Taylor Swift', 'Ed Sheeran', 'Taylor Swift',
        'Taylor Swift', 'Ed Sheeran', 'BTS',
        'BTS'
    ],
    'venue': [
        'MSG', 'MSG', 'MSG',
        'Staples Center', 'MSG', 'Staples Center',
        'MSG'
    ]
}

concerts_df = pd.DataFrame(concerts_data)

# Convert date column to datetime
concerts_df['date'] = pd.to_datetime(concerts_df['date'])

# Sample artists and venues as Series
artists = pd.Series(['Taylor Swift', 'Ed Sheeran', 'BTS'], name='artist')
venues = pd.Series(['MSG', 'Staples Center'], name='venue')

# print(concerts_df)

year_month = []
for date in concerts_df['date']:
    month = date.month
    year = date.year
    ym = str(year) + '-' + str(month)
    year_month.append(ym)

year_month1 = pd.to_datetime(year_month)
# print(year_month1)

artist_venue_pairs = pd.MultiIndex.from_product(
    [artists, venues], names=['artist', 'venue']
).to_frame(index=False)

# print(artist_venue_pairs)

# Add year_month column to concerts_df
concerts_df['year_month'] = year_month

# Group by year_month, artist, and venue, and count concerts
grouped = concerts_df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='concert_count')

# Pivot the grouped data into a wide format
wide_table = grouped.pivot(index='year_month', columns=['artist', 'venue'], values='concert_count')

# Ensure all (artist, venue) pairs are included
wide_table = wide_table.reindex(columns=pd.MultiIndex.from_frame(artist_venue_pairs), fill_value=0)

# Fill missing values with zeros
wide_table = wide_table.fillna(0)

print(wide_table)





