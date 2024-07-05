class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        critical_points = []
        index = 1
        prev = head
        current = head.next
        next_node = head.next.next

        while next_node:
            if (current.val > prev.val and current.val > next_node.val) or (current.val < prev.val and current.val < next_node.val):
                critical_points.append(index)
            prev = current
            current = next_node
            next_node = next_node.next
            index += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        return [min_distance, max_distance]
