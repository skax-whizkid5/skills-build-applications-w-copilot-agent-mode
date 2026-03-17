import { useEffect, useState } from 'react';
import ResourceTableCard from './ResourceTableCard';
import { normalizeApiList } from '../utils/normalizeApiList';

function Activities({ apiBaseUrl }) {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [reloadToken, setReloadToken] = useState(0);
  const activitiesApiUrl = `${apiBaseUrl.replace(/\/$/, '')}/api/activities/`;

  useEffect(() => {
    const controller = new AbortController();

    const fetchActivities = async () => {
      try {
        setLoading(true);
        setError('');

        const response = await fetch(activitiesApiUrl, {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const items = normalizeApiList(data);
        console.log('[Activities] endpoint:', activitiesApiUrl);
        console.log('[Activities] API payload:', data);
        console.log('[Activities] normalized items:', items);
        setActivities(items);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(`활동 데이터를 불러오지 못했습니다. (${err.message})`);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchActivities();

    return () => controller.abort();
  }, [activitiesApiUrl, reloadToken]);

  const columns = [
    {
      key: 'object_id',
      label: 'object_id',
      cellClassName: 'mono-id',
      render: (value, row) => value || row.id || '-',
    },
    { key: 'user', label: 'user', cellClassName: 'mono-id' },
    { key: 'activity_type', label: 'activity_type' },
    { key: 'duration_minutes', label: 'duration_minutes' },
    { key: 'calories_burned', label: 'calories_burned' },
    {
      key: 'performed_at',
      label: 'performed_at',
      render: (value) => (value ? new Date(value).toLocaleString() : '-'),
    },
  ];

  return (
    <ResourceTableCard
      title="Activities"
      endpoint={activitiesApiUrl}
      rows={activities}
      columns={columns}
      loading={loading}
      error={error}
      onRefresh={() => setReloadToken((current) => current + 1)}
    />
  );
}

export default Activities;
