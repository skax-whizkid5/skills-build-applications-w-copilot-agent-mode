import { useEffect, useState } from 'react';
import ResourceTableCard from './ResourceTableCard';
import { normalizeApiList } from '../utils/normalizeApiList';

function Workouts({ apiBaseUrl }) {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [reloadToken, setReloadToken] = useState(0);
  const workoutsApiUrl = `${apiBaseUrl.replace(/\/$/, '')}/api/workouts/`;

  useEffect(() => {
    const controller = new AbortController();

    const fetchWorkouts = async () => {
      try {
        setLoading(true);
        setError('');

        const response = await fetch(workoutsApiUrl, {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const items = normalizeApiList(data);
        console.log('[Workouts] endpoint:', workoutsApiUrl);
        console.log('[Workouts] API payload:', data);
        console.log('[Workouts] normalized items:', items);
        setWorkouts(items);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(`운동 데이터를 불러오지 못했습니다. (${err.message})`);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchWorkouts();

    return () => controller.abort();
  }, [workoutsApiUrl, reloadToken]);

  const columns = [
    {
      key: 'object_id',
      label: 'object_id',
      cellClassName: 'mono-id',
      render: (value, row) => value || row.id || '-',
    },
    { key: 'user', label: 'user', cellClassName: 'mono-id' },
    { key: 'title', label: 'title' },
    { key: 'difficulty', label: 'difficulty' },
    { key: 'target_reps', label: 'target_reps' },
    {
      key: 'is_completed',
      label: 'is_completed',
      render: (value) => (value ? '완료' : '미완료'),
    },
  ];

  return (
    <ResourceTableCard
      title="Workouts"
      endpoint={workoutsApiUrl}
      rows={workouts}
      columns={columns}
      loading={loading}
      error={error}
      onRefresh={() => setReloadToken((current) => current + 1)}
    />
  );
}

export default Workouts;
