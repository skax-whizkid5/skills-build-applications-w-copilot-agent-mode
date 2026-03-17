import { useEffect, useState } from 'react';
import ResourceTableCard from './ResourceTableCard';
import { normalizeApiList } from '../utils/normalizeApiList';

function Users({ apiBaseUrl }) {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [reloadToken, setReloadToken] = useState(0);
  const usersApiUrl = `${apiBaseUrl.replace(/\/$/, '')}/api/users/`;

  useEffect(() => {
    const controller = new AbortController();

    const fetchUsers = async () => {
      try {
        setLoading(true);
        setError('');

        const response = await fetch(usersApiUrl, {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const items = normalizeApiList(data);
        console.log('[Users] endpoint:', usersApiUrl);
        console.log('[Users] API payload:', data);
        console.log('[Users] normalized items:', items);
        setUsers(items);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(`사용자 데이터를 불러오지 못했습니다. (${err.message})`);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();

    return () => controller.abort();
  }, [usersApiUrl, reloadToken]);

  const columns = [
    {
      key: 'object_id',
      label: 'object_id',
      cellClassName: 'mono-id',
      render: (value, row) => value || row.id || '-',
    },
    { key: 'name', label: 'name' },
    { key: 'email', label: 'email' },
    {
      key: 'team',
      label: 'team',
      cellClassName: 'mono-id',
      render: (value) => value || '-',
    },
    { key: 'total_points', label: 'total_points' },
  ];

  return (
    <ResourceTableCard
      title="Users"
      endpoint={usersApiUrl}
      rows={users}
      columns={columns}
      loading={loading}
      error={error}
      onRefresh={() => setReloadToken((current) => current + 1)}
    />
  );
}

export default Users;
